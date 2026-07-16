from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.config import settings
from app.core.logger import logger
from app.database.database import Base, engine


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application startup and shutdown events.
    """

    logger.info(f"{settings.APP_NAME} starting up...")

    # Create database tables
    Base.metadata.create_all(bind=engine)

    # Future startup tasks:
    # - Initialize LLM clients
    # - Connect to vector database
    # - Load prompt templates
    # - Initialize caches

    yield

    logger.info(f"{settings.APP_NAME} shutting down...")

    # Future shutdown tasks:
    # - Close database connections
    # - Close HTTP clients
    # - Flush logs
