from fastapi import APIRouter

from app.core.config import settings
from app.core.logger import logger
from app.schemas.response import HealthResponse, RootResponse

router = APIRouter()


@router.get("/", response_model=RootResponse)
async def root():
    logger.info("Root endpoint accessed")

    return RootResponse(
        application=settings.APP_NAME,
        version="1.0.0",
        status="running",
    )


@router.get("/health", response_model=HealthResponse)
async def health_check():
    logger.info("Health endpoint accessed")

    return HealthResponse(
        status="healthy",
    )
