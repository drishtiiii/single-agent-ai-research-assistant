from app.core.logger import logger
from app.database.crud import (
    create_research_history,
    update_research_status,
)
from app.database.database import SessionLocal
from app.exports.markdown_exporter import MarkdownExporter
from app.exports.pdf_exporter import PDFExporter
from app.graph.graph import research_graph


class ResearchService:
    """
    Service responsible for performing AI-powered research.
    """

    def __init__(self) -> None:
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

        db = SessionLocal()

        history = create_research_history(
            db=db,
            query=query,
            status="PENDING",
        )

        try:
            update_research_status(
                db=db,
                history=history,
                status="RUNNING",
            )

            logger.info("Running LangGraph workflow...")

            result = await research_graph.ainvoke(
                {
                    "query": query,
                    "tool": "",
                    "context": "",
                    "report": "",
                    "score": 0,
                    "feedback": "",
                    "attempts": 0,
                }
            )

            final_report = result["report"]

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

            update_research_status(
                db=db,
                history=history,
                status="COMPLETED",
                report=final_report,
                markdown_path=markdown_path,
                pdf_path=pdf_path,
            )

            logger.info("Research completed.")

            return final_report

        except Exception:
            update_research_status(
                db=db,
                history=history,
                status="FAILED",
            )

            logger.exception("Research failed.")
            raise

        finally:
            db.close()
