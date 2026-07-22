from fastapi import APIRouter

from app.api.routes.health import router as health_router
from app.api.routes.history import router as history_router
from app.api.routes.llm import router as llm_router
from app.api.routes.research import router as research_router
from app.api.translate import router as translate_router

router = APIRouter()

# Health
router.include_router(
    health_router,
    tags=["Health"],
)

# Research
router.include_router(
    research_router,
    tags=["Research"],
)

# History
router.include_router(
    history_router,
    tags=["History"],
)

# LLM
router.include_router(
    llm_router,
    tags=["LLM"],
)

# Translation
router.include_router(
    translate_router,
    tags=["Translation"],
)