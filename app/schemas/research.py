from datetime import datetime

from pydantic import BaseModel


# -----------------------------
# Research Request
# -----------------------------
class ResearchRequest(BaseModel):
    query: str


# -----------------------------
# Research Response
# -----------------------------
class ResearchResponse(BaseModel):
    success: bool
    report: str


# -----------------------------
# Research History Item
# -----------------------------
class ResearchHistoryItem(BaseModel):
    id: int
    query: str
    markdown_path: str | None = None
    pdf_path: str | None = None
    created_at: datetime

    class Config:
        from_attributes = True


# -----------------------------
# Research History Response
# -----------------------------
class ResearchHistoryResponse(BaseModel):
    success: bool
    history: list[ResearchHistoryItem]