from fastapi import APIRouter, HTTPException

from app.core.logger import logger
from app.schemas.llm import LLMRequest, LLMResponse
from app.services.llm_service import LLMService

router = APIRouter()


@router.post("/test-llm", response_model=LLMResponse)
async def test_llm(request: LLMRequest):

    try:
        service = LLMService()

        response = await service.generate_response(prompt=request.prompt)

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
