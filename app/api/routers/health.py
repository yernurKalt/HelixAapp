from fastapi import APIRouter

from app.core.config import settings


router = APIRouter(
    prefix=f"{settings.API_PREFIX}/health",
    tags=["health"]
)


@router.get("")
async def get_status():
    return {
        "status": "ok",
        "app_name": settings.APP_NAME,
        "env": settings.ENV
    }