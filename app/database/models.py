from datetime import datetime,UTC

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text

from app.database.database import Base


class ResearchHistory(Base):
    """
    Database model for storing research reports.
    """

    __tablename__ = "research_history"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    query = Column(
        String,
        nullable=False,
    )

    report = Column(
        Text,
        nullable=False,
    )

    markdown_path = Column(
        String,
        nullable=True,
    )

    pdf_path = Column(
        String,
        nullable=True,
    )
    status = Column(
    String,
    default="PENDING",
    nullable=False,
    )

    created_at = Column(
        DateTime,
        default=lambda: datetime.now(UTC)
    )
   