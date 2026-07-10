from pydantic import BaseModel


class ResearchRequest(BaseModel):
    query: str


class ResearchResponse(BaseModel):
    success: bool
    report: str