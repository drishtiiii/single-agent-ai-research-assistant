from pathlib import Path

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.logger import logger
from app.database.crud import (
    delete_research_history,
    get_all_research_history,
    get_research_history_by_id,
    search_research_history,
)
from app.dependencies.database import get_db
from app.exceptions.custom_exceptions import (
    ResearchNotFoundError,
)
from app.schemas.research import (
    DeleteResearchResponse,
    ResearchDetailResponse,
    ResearchHistoryResponse,
)

router = APIRouter()

@router.get(
    "/history",
    response_model=ResearchHistoryResponse,
)
async def research_history(
    db: Session = Depends(get_db),
):
    history = get_all_research_history(db)

    return ResearchHistoryResponse(
        success=True,
        history=history,
    )

@router.get(
    "/history/search",
    response_model=ResearchHistoryResponse,
)
async def search_history(
    query: str,
    db: Session = Depends(get_db),
):
    history = search_research_history(
        db=db,
        query=query,
    )

    return ResearchHistoryResponse(
        success=True,
        history=history,
    )
@router.get(
    "/history/{history_id}",
    response_model=ResearchDetailResponse,
)
async def get_history_by_id(
    history_id: int,
    db: Session = Depends(get_db),
):
    history = get_research_history_by_id(
        db=db,
        history_id=history_id,
    )

    if history is None:
        raise ResearchNotFoundError(
            history_id=history_id,
        )

    return ResearchDetailResponse(
        success=True,
        history=history,
    )
@router.delete(
    "/history/{history_id}",
    response_model=DeleteResearchResponse,
)
async def delete_history(
    history_id: int,
    db: Session = Depends(get_db),
):
    history = get_research_history_by_id(
        db=db,
        history_id=history_id,
    )

    if history is None:
        raise ResearchNotFoundError(
            history_id=history_id,
        )

    if history.markdown_path:
        markdown = Path(history.markdown_path)

        if markdown.exists():
            markdown.unlink()

    if history.pdf_path:
        pdf = Path(history.pdf_path)

        if pdf.exists():
            pdf.unlink()

    delete_research_history(
        db=db,
        history=history,
    )

    logger.info(
        f"Research report {history_id} deleted."
    )

    return DeleteResearchResponse(
        success=True,
        message="Research report deleted successfully.",
    )