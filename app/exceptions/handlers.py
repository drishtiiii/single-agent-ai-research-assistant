from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.core.logger import logger
from app.exceptions.custom_exceptions import (
    ResearchNotFoundError,
)


def register_exception_handlers(
    app: FastAPI,
):
    """
    Register global exception handlers.
    """

    @app.exception_handler(
        ResearchNotFoundError
    )
    async def research_not_found_handler(
        request: Request,
        exc: ResearchNotFoundError,
    ):

        return JSONResponse(
            status_code=404,
            content={
                "success": False,
                "message": str(exc),
            },
        )

    @app.exception_handler(Exception)
    async def global_exception_handler(
        request: Request,
        exc: Exception,
    ):

        logger.exception(exc)

        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "message": "Internal Server Error",
            },
        )