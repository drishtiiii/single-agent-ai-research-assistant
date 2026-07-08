from fastapi import APIRouter

from app.api.routes import router as base_router

router = APIRouter(prefix="/api/v1", tags=["API v1"])

router.include_router(base_router)