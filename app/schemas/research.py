from datetime import datetime

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    field_validator,
)


# -----------------------------
# Research Request
# -----------------------------
class ResearchRequest(BaseModel):
    query: str = Field(
        ...,
        min_length=5,
        max_length=500,
        description="Research query",
        examples=[
            "Latest developments in Quantum Computing",
        ],
    )

    @field_validator("query")
    @classmethod
    def validate_query(
        cls,
        value: str,
    ) -> str:

        value = value.strip()

        if not value:
            raise ValueError("Query cannot be empty.")

        return value


# -----------------------------
# Research Response
# -----------------------------
class ResearchResponse(BaseModel):
    success: bool
    job_id: int
    report: str


# -----------------------------
# Research History Item
# -----------------------------
class ResearchHistoryItem(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    query: str
    report: str
    status: str
    markdown_path: str | None = None
    pdf_path: str | None = None
    created_at: datetime


# -----------------------------
# Research History Response
# -----------------------------
class ResearchHistoryResponse(BaseModel):
    success: bool
    history: list[ResearchHistoryItem]


# -----------------------------
# Research Detail Response
# -----------------------------
class ResearchDetailResponse(BaseModel):
    success: bool
    history: ResearchHistoryItem


# -----------------------------
# Delete Research Response
# -----------------------------
class DeleteResearchResponse(BaseModel):
    success: bool
    message: str
