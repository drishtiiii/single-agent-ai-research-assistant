from app.core.logger import logger
from app.services.research_service import ResearchService


async def run_research(
    history_id: int,
    query: str,
):
    """
    Background task responsible for generating
    a research report.
    """

    logger.info(f"Background research started: {query} (Job ID: {history_id})")

    service = ResearchService()

    await service.research(
        history_id=history_id,
        query=query,
    )

    logger.info(f"Background research completed: {query} (Job ID: {history_id})")
