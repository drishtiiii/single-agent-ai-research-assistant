from collections.abc import Generator

from sqlalchemy.orm import Session

from app.database.database import SessionLocal


def get_db() -> Generator[Session]:
    """
    FastAPI dependency that provides
    a database session.
    """

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()
