from sqlalchemy.orm import Session

from app.database.crud import (
    get_all_research_history,
    get_research_history_by_id,
    search_research_history,
)


class DatabaseTool:
    """
    Tool responsible for retrieving research history
    from the local database.
    """

    def get_all(
        self,
        db: Session,
    ):
        return get_all_research_history(db)

    def search(
        self,
        db: Session,
        query: str,
    ):
        return search_research_history(
            db=db,
            query=query,
        )

    def get_by_id(
        self,
        db: Session,
        history_id: int,
    ):
        return get_research_history_by_id(
            db=db,
            history_id=history_id,
        )
