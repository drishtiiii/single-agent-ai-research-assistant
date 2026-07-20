from app.core.logger import logger
from app.core.request_id import generate_request_id
from app.core.timer import Timer
from app.database.crud import (
    get_research_history_by_id,
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
        history_id: int,
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

        history = get_research_history_by_id(
            db=db,
            history_id=history_id,
        )
        if history is None:
            raise ValueError(f"Research history {history_id} not found.")

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
                    "clarification": "",
                    "needs_input": False,
                }
            )

            # -----------------------------
            # # DEBUG OUTPUT
            # # -----------------------------
            logger.info("========== GRAPH RESULT ==========")
            logger.info(result)
            print("\n========== GRAPH RESULT ==========")
            print(result)
            print("needs_input :", result.get("needs_input"))
            print("clarification :", result.get("clarification"))
            print("report length :", len(result.get("report", "")))
            print("=================================\n")
            final_report = result.get("report", "")
            if result.get("needs_input"):
                logger.warning(
                    "[{}] Graph requested clarification: {}",
                    request_id,
                    result.get("clarification"),
                )
                update_research_status(
                    db=db,
                    history=history,
                    status="NEEDS_INPUT",
                )
                return result.get("clarification", "More information is required.")

            if not final_report.strip():
                raise ValueError("LangGraph returned an empty report.")

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
