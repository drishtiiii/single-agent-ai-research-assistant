from typing import TypedDict


class ResearchState(TypedDict):
    query: str
    context: str
    report: str
    score: int
    feedback: str