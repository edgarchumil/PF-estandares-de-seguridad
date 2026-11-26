"""Export application data without credentials and initialize an empty deployment."""

import argparse
import asyncio
import base64
import json
import os
import secrets
from datetime import UTC, date, datetime
from pathlib import Path
from typing import Any
from uuid import UUID

from sqlalchemy import Column, Date, DateTime, LargeBinary, Uuid, func, select, text
from sqlalchemy.ext.asyncio import AsyncConnection, AsyncEngine

from app.core.config import settings
from app.core.database import dispose_engine, engine
from app.models import Base
from app.security.passwords import hash_password
from app.seed import DEMO_USERS

EXCLUDED_TABLES = {"sessions", "password_reset_tokens"}
PASSWORD_FIELDS = {"password_hash", "mfa_secret"}
SENSITIVE_KEYS = {
    "password", "password_hash", "secret", "secret_key", "mfa_secret", "mfa_code",
    "token", "token_hash", "refresh_token", "refresh_token_hash", "api_key", "openai_api_key",
}
SNAPSHOT_PATH = Path(__file__).resolve().parents[1] / "data" / "render.snapshot.json"


def scrub_json(value: Any) -> Any:
    if isinstance(value, dict):
        return {
            key: scrub_json(item) for key, item in value.items()
            if key.lower() not in SENSITIVE_KEYS
        }
    if isinstance(value, list):
        return [scrub_json(item) for item in value]
    return value


def encode(value: Any) -> Any:
    if isinstance(value, UUID):
        return str(value)
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    if isinstance(value, bytes):
        return base64.b64encode(value).decode("ascii")
    return value


def decode(column: Column[Any], value: Any) -> Any:
    if value is None:
        return None
    if isinstance(column.type, Uuid):
        return UUID(value)
    if isinstance(column.type, DateTime):
        return datetime.fromisoformat(value)
    if isinstance(column.type, Date):
        return date.fromisoformat(value)
    if isinstance(column.type, LargeBinary):
        return base64.b64decode(value, validate=True)
    return value


async def export_snapshot(connection: AsyncConnection, path: Path) -> dict[str, int]:
    tables: dict[str, list[dict[str, Any]]] = {}
    for table in Base.metadata.sorted_tables:
        if table.name in EXCLUDED_TABLES:
            continue
        records = []
        for result in (await connection.execute(select(table))).mappings():
            row = dict(result)
            if table.name == "users":
                for key in PASSWORD_FIELDS:
                    row.pop(key, None)
                row.update(mfa_enabled=False, failed_login_attempts=0, locked_until=None)
            if table.name == "audit_logs":
                row.update(ip_address=None, user_agent=None, correlation_id=None)
                row["changes"] = scrub_json(row["changes"])
            if table.name == "system_settings":
                if row["key"].lower() in SENSITIVE_KEYS:
                    raise RuntimeError(
                        "A secret setting must be moved to Render environment variables"
                    )
                row["value"] = scrub_json(row["value"])
            if table.name == "reports" and row["status"] == "completed":
                if row["pdf_content"] is None:
                    root = Path(settings.report_storage_path).resolve()
                    pdf = (root / (row["storage_key"] or "")).resolve()
                    if root not in pdf.parents or not pdf.is_file():
                        raise RuntimeError(f"Missing report PDF: {row['id']}")
                    row["pdf_content"] = pdf.read_bytes()
            records.append({key: encode(value) for key, value in row.items()})
        tables[table.name] = records
    payload = {
        "format_version": 1,
        "exported_at": datetime.now(UTC).isoformat(),
        "excluded_tables": sorted(EXCLUDED_TABLES),
        "tables": tables,
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return {name: len(rows) for name, rows in tables.items()}


async def restore_snapshot(
    target_engine: AsyncEngine, path: Path, password: str
) -> bool:
    async with target_engine.begin() as connection:
        if connection.dialect.name == "postgresql":
            await connection.execute(text("SELECT pg_advisory_xact_lock(72401935)"))
        # Never merge, overwrite, or reinitialize an existing database on a redeploy.
        for table in Base.metadata.sorted_tables:
            if await connection.scalar(select(func.count()).select_from(table)):
                print("Existing database preserved; initial import skipped.")
                return False
        if len(password) < 12:
            raise RuntimeError("Set DEMO_PASSWORD in Render to at least 12 characters")
        payload = json.loads(path.read_text(encoding="utf-8"))
        expected = set(Base.metadata.tables) - EXCLUDED_TABLES
        if payload.get("format_version") != 1 or set(payload["tables"]) != expected:
            raise RuntimeError("Snapshot format or table list does not match the application")
        demo_emails = {email for email, _, _ in DEMO_USERS}
        if not any(
            row["email"] == "administrador@demo.local" and row["is_superadmin"]
            for row in payload["tables"]["users"]
        ):
            raise RuntimeError("Snapshot has no bootstrap administrator")
        for table in Base.metadata.sorted_tables:
            if table.name in EXCLUDED_TABLES:
                continue
            rows = []
            for record in payload["tables"][table.name]:
                if table.name == "users" and PASSWORD_FIELDS.intersection(record):
                    raise RuntimeError("Snapshot must not contain credentials")
                row = {key: decode(table.c[key], value) for key, value in record.items()}
                if table.name == "users":
                    initial = password if row["email"] in demo_emails else secrets.token_urlsafe(48)
                    row.update(
                        password_hash=hash_password(initial), mfa_secret=None,
                        mfa_enabled=False, failed_login_attempts=0, locked_until=None,
                    )
                rows.append(row)
            # Small batches also work with PostgreSQL's bind parameter limit.
            for offset in range(0, len(rows), 100):
                await connection.execute(table.insert(), rows[offset:offset + 100])
        for table in Base.metadata.sorted_tables:
            count = await connection.scalar(select(func.count()).select_from(table))
            if count != len(payload["tables"].get(table.name, [])):
                raise RuntimeError(f"Import count mismatch: {table.name}")
    print("Initial database imported; subsequent deployments will preserve it.")
    return True


async def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=["export", "restore"])
    parser.add_argument("--path", type=Path, default=SNAPSHOT_PATH)
    args = parser.parse_args()
    try:
        if args.action == "export":
            async with engine.connect() as connection:
                if connection.dialect.name == "postgresql":
                    connection = await connection.execution_options(
                        isolation_level="REPEATABLE READ"
                    )
                async with connection.begin():
                    counts = await export_snapshot(connection, args.path)
                    print(json.dumps(counts, indent=2))
        else:
            await restore_snapshot(engine, args.path, os.getenv("DEMO_PASSWORD", ""))
    finally:
        await dispose_engine()


if __name__ == "__main__":
    asyncio.run(main())
