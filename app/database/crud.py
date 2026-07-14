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
    page: int = 1,
    size: int = 10,
) -> list[ResearchHistory]:
    """
    Retrieve paginated research history.
    """

    # Prevent invalid pagination values
    page = max(page, 1)
    size = max(size, 1)

    offset = (page - 1) * size

    return (
        db.query(ResearchHistory)
        .order_by(ResearchHistory.created_at.desc())
        .offset(offset)
        .limit(size)
        .all()
    )


def search_research_history(
    db: Session,
    query: str,
) -> list[ResearchHistory]:
    """
    Search research history by query.
    """

    return (
        db.query(ResearchHistory)
        .filter(
            ResearchHistory.query.ilike(f"%{query}%")
        )
        .order_by(
            ResearchHistory.created_at.desc()
        )
        .all()
    )


def get_research_history_by_id(
    db: Session,
    history_id: int,
) -> ResearchHistory | None:
    """
    Retrieve a report by ID.
    """

    return (
        db.query(ResearchHistory)
        .filter(
            ResearchHistory.id == history_id
        )
        .first()
    )


def delete_research_history(
    db: Session,
    history: ResearchHistory,
) -> None:
    """
    Delete a research report.
    """

    db.delete(history)
    db.commit()