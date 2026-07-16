from fastapi import APIRouter

from .health import router as health_router
from .history import router as history_router
from .llm import router as llm_router
from .research import router as research_router

router = APIRouter()

router.include_router(health_router)
router.include_router(llm_router)
router.include_router(research_router)
router.include_router(history_router)
