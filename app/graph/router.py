from app.graph.state import ResearchState

MAX_ATTEMPTS = 2


def evaluation_router(
    state: ResearchState,
) -> str:
    """
    Decide whether to accept or improve the report.
    """

    if state["score"] >= 8:
        return "accept"

    if state["attempts"] >= MAX_ATTEMPTS:
        return "accept"

    return "improve"
