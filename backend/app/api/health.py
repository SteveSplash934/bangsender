from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from redis.asyncio import Redis
from app.db.session import get_db
from app.core.config import settings

# This is a specific router just for health checks
router = APIRouter()

@router.get("/health")
async def health_check(db: AsyncSession = Depends(get_db)):
    """
    Checks the health of the Backend, Database (PostgreSQL), and Cache (Redis).
    """
    health_status = {
        "status": "healthy",
        "database": "unknown",
        "redis": "unknown",
        "errors": []
    }

    # 1. Check PostgreSQL
    try:
        await db.execute(text("SELECT 1"))
        health_status["database"] = "connected"
    except Exception as e:
        health_status["status"] = "unhealthy"
        health_status["database"] = "disconnected"
        health_status["errors"].append(f"DB Error: {str(e)}")

    # 2. Check Redis
    try:
        redis_client = Redis(
            host=settings.REDIS_HOST, 
            port=settings.REDIS_PORT, 
            socket_connect_timeout=1
        )
        await redis_client.ping()
        await redis_client.close()
        health_status["redis"] = "connected"
    except Exception as e:
        health_status["status"] = "unhealthy"
        health_status["redis"] = "disconnected"
        health_status["errors"].append(f"Redis Error: {str(e)}")

    return health_status

@router.get("/")
async def root():
    return {"message": "NovaMailer Backend is running."}