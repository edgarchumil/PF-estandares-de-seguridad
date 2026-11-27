import logging
from typing import Literal

from fastapi import APIRouter, Response, status
from sqlalchemy import text

from app.core.config import settings
from app.core.database import engine
from app.core.redis import redis_client
from app.schemas.health import DependencyStatus, ReadinessResponse

router = APIRouter(prefix="/health", tags=["salud"])
logger = logging.getLogger(__name__)


async def database_is_ready() -> bool:
    try:
        async with engine.connect() as connection:
            await connection.execute(text("SELECT 1"))
        return True
    except Exception as exc:  # no se exponen credenciales ni URLs de conexión
        logger.warning("Database readiness check failed (%s)", type(exc).__name__)
        return False


async def redis_is_ready() -> bool:
    try:
        await redis_client.ping()
        return True
    except Exception as exc:  # no se exponen credenciales ni URLs de conexión
        logger.warning("Redis readiness check failed (%s)", type(exc).__name__)
        return False


@router.get("/live")
async def liveness() -> dict[str, str]:
    return {"status": "ok"}


@router.get("/ready", response_model=ReadinessResponse)
async def readiness(response: Response) -> ReadinessResponse:
    checks: dict[str, DependencyStatus] = {}
    checks["database"] = DependencyStatus(status="ok" if await database_is_ready() else "error")
    # Background reports run inside the API and never use the Celery broker.
    if settings.report_execution_mode == "celery":
        checks["redis"] = DependencyStatus(status="ok" if await redis_is_ready() else "error")

    overall: Literal["ok", "degraded"] = (
        "ok" if all(item.status == "ok" for item in checks.values()) else "degraded"
    )
    if overall == "degraded":
        response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE
    return ReadinessResponse(status=overall, services=checks)
