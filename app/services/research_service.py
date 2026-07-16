from app.core.logger import logger
from app.core.request_id import generate_request_id
from app.core.timer import Timer
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
        Perform AI-powered research using the LangGraph workflow.
        """

        request_id = generate_request_id()
        timer = Timer()

        logger.info(
            "[{}] Research started: {}",
            request_id,
            query,
        )

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

            logger.info(
                "[{}] Running LangGraph workflow...",
                request_id,
            )

            result = await research_graph.ainvoke(
                {
                    "query": query,
                    "tool": "",
                    "context": "",
                    "report": "",
                    "score": 0,
                    "feedback": "",
                    "attempts": 0,
                    "request_id": request_id,
                    "use_memory": False,
                }
            )

            final_report = result["report"]

            logger.info(
                "[{}] Exporting Markdown...",
                request_id,
            )

            markdown_path = self.exporter.export(
                title=query,
                report=final_report,
            )

            logger.info(
                "[{}] Exporting PDF...",
                request_id,
            )

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

            logger.info(
                "[{}] Research completed successfully in {:.3f} sec",
                request_id,
                timer.elapsed(),
            )

            return final_report

        except Exception:
            update_research_status(
                db=db,
                history=history,
                status="FAILED",
            )

            logger.exception(
                "[{}] Research failed after {:.3f} sec",
                request_id,
                timer.elapsed(),
            )

            raise

        finally:
            db.close()