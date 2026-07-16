from app.core.logger import logger
from app.services.research_service import ResearchService


async def run_research(query: str):
    """
    Background task responsible for generating
    a research report.
    """

    logger.info(f"Background research started: {query}")

    service = ResearchService()

    await service.research(
        query=query,
    )

    logger.info(f"Background research completed: {query}")
