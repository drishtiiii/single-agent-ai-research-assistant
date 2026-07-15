from fastapi import APIRouter, BackgroundTasks
from app.tasks.research_tasks import run_research
from app.schemas.research import (
    ResearchRequest,
    ResearchResponse,
)
from app.services.research_service import ResearchService

router = APIRouter()


@router.post(
    "/research",
    response_model=ResearchResponse,
)
async def research(
    request: ResearchRequest,
    background_tasks: BackgroundTasks,
):

    background_tasks.add_task(
        run_research,
        request.query,
    )

    return ResearchResponse(
        success=True,
        report=(
            "Research has started in the background. "
            "Please check your history shortly."
        ),
    )