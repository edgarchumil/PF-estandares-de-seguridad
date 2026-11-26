import json
from pathlib import Path

import pytest
from fastapi import FastAPI
from httpx import ASGITransport, AsyncClient
from sqlalchemy import event, func, select
from sqlalchemy.ext.asyncio import create_async_engine

from app.deployment_data import restore_snapshot
from app.frontend import mount_frontend
from app.models import Base, User
from app.security.passwords import verify_password

SNAPSHOT = Path(__file__).resolve().parents[1] / "data" / "render.snapshot.json"


async def test_restore_preserves_content_and_never_overwrites_existing_data() -> None:
    engine = create_async_engine("sqlite+aiosqlite:///:memory:")

    @event.listens_for(engine.sync_engine, "connect")
    def enforce_foreign_keys(connection, _):  # type: ignore[no-untyped-def]
        connection.execute("PRAGMA foreign_keys=ON")

    try:
        async with engine.begin() as connection:
            await connection.run_sync(Base.metadata.create_all)
        password = "render-test-password-2026"
        assert await restore_snapshot(engine, SNAPSHOT, password)
        payload = json.loads(SNAPSHOT.read_text(encoding="utf-8"))
        async with engine.connect() as connection:
            for table in Base.metadata.sorted_tables:
                count = await connection.scalar(select(func.count()).select_from(table))
                assert count == len(payload["tables"].get(table.name, []))
            user = (await connection.execute(
                select(User.__table__).where(User.email == "administrador@demo.local")
            )).mappings().one()
            original_hash = user["password_hash"]
            assert verify_password(password, original_hash)
            assert not user["mfa_enabled"]
            assert user["mfa_secret"] is None
            for row in payload["tables"]["reports"]:
                if row["status"] == "completed":
                    assert row["pdf_content"]
        assert not await restore_snapshot(engine, SNAPSHOT, "changed-password-on-redeploy")
        async with engine.connect() as connection:
            assert await connection.scalar(
                select(User.password_hash).where(User.email == "administrador@demo.local")
            ) == original_hash
    finally:
        await engine.dispose()


async def test_invalid_password_leaves_database_empty() -> None:
    engine = create_async_engine("sqlite+aiosqlite:///:memory:")
    try:
        async with engine.begin() as connection:
            await connection.run_sync(Base.metadata.create_all)
        with pytest.raises(RuntimeError, match="DEMO_PASSWORD"):
            await restore_snapshot(engine, SNAPSHOT, "short")
        async with engine.connect() as connection:
            assert await connection.scalar(select(func.count()).select_from(User)) == 0
    finally:
        await engine.dispose()


def test_snapshot_does_not_publish_authentication_secrets() -> None:
    payload = json.loads(SNAPSHOT.read_text(encoding="utf-8"))
    assert "sessions" not in payload["tables"]
    assert "password_reset_tokens" not in payload["tables"]
    for user in payload["tables"]["users"]:
        assert "password_hash" not in user
        assert "mfa_secret" not in user
    for audit in payload["tables"]["audit_logs"]:
        assert audit["ip_address"] is None
        assert audit["user_agent"] is None


async def test_frontend_routes_keep_api_errors_and_files_separate(tmp_path: Path) -> None:
    (tmp_path / "assets").mkdir()
    (tmp_path / "assets" / "app.js").write_text("console.log('ok')", encoding="utf-8")
    (tmp_path / "index.html").write_text("<html>CGSI</html>", encoding="utf-8")
    app = FastAPI()

    @app.get("/api/v1/health")
    async def health() -> dict[str, str]:
        return {"status": "ok"}

    mount_frontend(app, tmp_path)
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        assert "CGSI" in (await client.get("/")).text
        assert "CGSI" in (await client.get("/panel")).text
        assert (await client.get("/assets/app.js")).status_code == 200
        assert (await client.get("/api/v1/health")).json() == {"status": "ok"}
        assert (await client.get("/api/v1/missing")).status_code == 404
        assert (await client.get("/missing.js")).status_code == 404
        assert (await client.get("/%2e%2e/outside")).status_code == 404
