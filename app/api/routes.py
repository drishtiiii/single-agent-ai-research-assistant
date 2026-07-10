from fastapi import APIRouter, HTTPException

from app.core.config import settings
from app.core.logger import logger
from app.schemas.response import RootResponse, HealthResponse
from app.schemas.llm import LLMRequest, LLMResponse
from app.services.llm_service import LLMService

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


@router.post("/test-llm", response_model=LLMResponse)
async def test_llm(request: LLMRequest):

    print(">>> TEST LLM ENDPOINT HIT <<<")

    try:
        service = LLMService()

        response = await service.generate_response(
            prompt=request.prompt
        )

        return LLMResponse(
            success=True,
            response=response,
        )

    except Exception as e:
        logger.exception(e)
        raise HTTPException(
            status_code=500,
            detail=str(e),
        )