from sqlalchemy.orm import Session

from app.database.models import ResearchHistory


def create_research_history(
    db: Session,
    query: str,
    report: str,
    markdown_path: str | None = None,
    pdf_path: str | None = None,
) -> ResearchHistory:
    """
    Save a research report to the database.
    """

    history = ResearchHistory(
        query=query,
        report=report,
        markdown_path=markdown_path,
        pdf_path=pdf_path,
    )

    db.add(history)
    db.commit()
    db.refresh(history)

    return history


def get_all_research_history(
    db: Session,
) -> list[ResearchHistory]:
    """
    Retrieve all saved research reports ordered by newest first.
    """

    return (
        db.query(ResearchHistory)
        .order_by(ResearchHistory.created_at.desc())
        .all()
    )