from fastapi import APIRouter, BackgroundTasks

from app.database.crud import create_research_history
from app.database.database import SessionLocal
from app.schemas.research import (
    ResearchRequest,
    ResearchResponse,
)
from app.tasks.research_tasks import run_research

router = APIRouter()


@router.post(
    "/research",
    response_model=ResearchResponse,
)
async def research(
    request: ResearchRequest,
    background_tasks: BackgroundTasks,
):
    db = SessionLocal()

    try:
        # Create the research job first
        history = create_research_history(
            db=db,
            query=request.query,
            status="PENDING",
        )

        # Start the background task with the job ID
        background_tasks.add_task(
            run_research,
            history.id,
            request.query,
        )

        return ResearchResponse(
            success=True,
            job_id=history.id,
            report=(
                "Research has started in the background. "
                "Please check your history shortly."
            ),
        )

    finally:
        db.close()