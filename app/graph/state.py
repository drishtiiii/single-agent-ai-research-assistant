from typing import TypedDict


class ResearchState(TypedDict):
    query: str

    tool: str

    context: str

    report: str

    score: int

    feedback: str

    attempts: int

    request_id: str

    use_memory: bool
