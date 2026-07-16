from pathlib import Path

from fastapi import APIRouter, HTTPException

from app.core.config import settings
from app.core.logger import logger
from app.database.crud import (
    delete_research_history,
    get_all_research_history,
    get_research_history_by_id,
    search_research_history,
)
from app.database.database import SessionLocal
from app.schemas.llm import LLMRequest, LLMResponse
from app.schemas.research import (
    DeleteResearchResponse,
    ResearchDetailResponse,
    ResearchHistoryResponse,
    ResearchRequest,
    ResearchResponse,
)
from app.schemas.response import HealthResponse, RootResponse
from app.services.llm_service import LLMService
from app.services.research_service import ResearchService

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


@router.post(
    "/research",
    response_model=ResearchResponse,
)
async def research(request: ResearchRequest):

    service = ResearchService()

    report = await service.research(
        query=request.query,
    )

    return ResearchResponse(
        success=True,
        report=report,
    )


@router.get(
    "/history",
    response_model=ResearchHistoryResponse,
)
async def research_history():

    db = SessionLocal()

    try:
        history = get_all_research_history(db)

        return ResearchHistoryResponse(
            success=True,
            history=history,
        )

    except Exception as e:
        logger.exception(e)
        raise HTTPException(
            status_code=500,
            detail=str(e),
        )

    finally:
        db.close()


# -------------------------
# Search History
# -------------------------
@router.get(
    "/history/search",
    response_model=ResearchHistoryResponse,
)
async def search_history(
    query: str,
):

    db = SessionLocal()

    try:
        history = search_research_history(
            db=db,
            query=query,
        )

        return ResearchHistoryResponse(
            success=True,
            history=history,
        )

    except Exception as e:
        logger.exception(e)
        raise HTTPException(
            status_code=500,
            detail=str(e),
        )

    finally:
        db.close()


# -------------------------
# Get History by ID
# -------------------------
@router.get(
    "/history/{history_id}",
    response_model=ResearchDetailResponse,
)
async def get_history_by_id(
    history_id: int,
):

    db = SessionLocal()

    try:
        history = get_research_history_by_id(
            db=db,
            history_id=history_id,
        )

        if history is None:
            raise HTTPException(
                status_code=404,
                detail="Research report not found.",
            )

        return ResearchDetailResponse(
            success=True,
            history=history,
        )

    except HTTPException:
        raise

    except Exception as e:
        logger.exception(e)
        raise HTTPException(
            status_code=500,
            detail=str(e),
        )

    finally:
        db.close()


# -------------------------
# Delete History
# -------------------------
@router.delete(
    "/history/{history_id}",
    response_model=DeleteResearchResponse,
)
async def delete_history(
    history_id: int,
):

    db = SessionLocal()

    try:
        history = get_research_history_by_id(
            db=db,
            history_id=history_id,
        )

        if history is None:
            raise HTTPException(
                status_code=404,
                detail="Research report not found.",
            )

        # Delete Markdown file
        if history.markdown_path:
            markdown = Path(history.markdown_path)

            if markdown.exists():
                markdown.unlink()

        # Delete PDF file
        if history.pdf_path:
            pdf = Path(history.pdf_path)

            if pdf.exists():
                pdf.unlink()

        delete_research_history(
            db=db,
            history=history,
        )

        logger.info(f"Research report {history_id} deleted.")

        return DeleteResearchResponse(
            success=True,
            message="Research report deleted successfully.",
        )

    except HTTPException:
        raise

    except Exception as e:
        logger.exception(e)
        raise HTTPException(
            status_code=500,
            detail=str(e),
        )

    finally:
        db.close()
