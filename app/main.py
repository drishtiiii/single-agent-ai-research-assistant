from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1 import router
from app.core.config import settings
from app.core.lifespan import lifespan
from app.exceptions.handlers import register_exception_handlers

app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0",
    description=(
        "A production-grade Single-Agent AI Research Assistant"
        "built with FastAPI, LangGraph, Groq, DuckDuckGo and Wikipedia."
    ),
    lifespan=lifespan,
)
# Register exception handlers
register_exception_handlers(app)

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # We'll restrict this after deployment
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API Routes
app.include_router(router)


@app.get("/")
async def root():
    return {
        "application": settings.APP_NAME,
        "version": "1.0.0",
        "status": "running",
        "docs": "/docs",
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy",
    }
