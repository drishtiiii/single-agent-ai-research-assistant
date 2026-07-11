from fastapi import FastAPI

from app.api.v1 import router
from app.core.config import settings
from app.core.lifespan import lifespan

app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0",
    description="A production-grade Single-Agent AI Research Assistant built with FastAPI and Groq.",
    lifespan=lifespan,
)

app.include_router(router)