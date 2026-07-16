from fastapi import FastAPI

from app.api.v1 import router
from app.core.config import settings
from app.core.lifespan import lifespan
from app.exceptions.handlers import register_exception_handlers

app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0",
    description=(
        "A production-grade Single-Agent AI Research Assistant"
        "built with FastAPI and Groq."
    ),
    lifespan=lifespan,
)
register_exception_handlers(app)

app.include_router(router)
