from app.core.logger import logger
from app.database.crud import create_research_history
from app.database.database import SessionLocal
from app.exports.markdown_exporter import MarkdownExporter
from app.exports.pdf_exporter import PDFExporter
from app.prompts.research_prompt import build_research_prompt
from app.services.llm_service import LLMService
from app.tools.search import SearchTool


class ResearchService:
    """
    Service responsible for performing AI-powered research.
    """

    def __init__(self) -> None:
        self.search = SearchTool()
        self.llm = LLMService()
        self.exporter = MarkdownExporter()
        self.pdf_exporter = PDFExporter()

        logger.info("Research Service initialized.")

    async def research(
        self,
        query: str,
    ) -> str:
        """
        Perform web research and generate a comprehensive answer.
        """

        logger.info(f"Research started for: {query}")

        # Search the web
        search_results = self.search.search(
            query=query,
            max_results=5,
        )

        # Build search context
        context = ""

        for index, result in enumerate(search_results, start=1):
            context += (
                f"\nResult {index}\n"
                f"Title: {result['title']}\n"
                f"URL: {result['url']}\n"
                f"Content: {result['body']}\n"
            )

        logger.info("Generating research report...")

        prompt = build_research_prompt(
            query=query,
            context=context,
        )

        response = await self.llm.generate_response(
            prompt=prompt,
        )

        # Append sources
        sources = "\n\n---\n\n## Sources\n\n"

        for index, result in enumerate(search_results, start=1):
            sources += (
                f"{index}. {result['title']}\n"
                f"{result['url']}\n\n"
            )

        final_report = response + sources

        # Export Markdown
        markdown_path = self.exporter.export(
            title=query,
            report=final_report,
        )

        # Export PDF
        pdf_path = self.pdf_exporter.export(
            title=query,
            report=final_report,
        )

        # Save to database
        db = SessionLocal()

        try:
            create_research_history(
                db=db,
                query=query,
                report=final_report,
                markdown_path=markdown_path,
                pdf_path=pdf_path,
            )
        finally:
            db.close()

        logger.info("Research completed.")

        return final_report