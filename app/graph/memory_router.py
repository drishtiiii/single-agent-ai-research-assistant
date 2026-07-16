from app.graph.state import ResearchState


def memory_router(
    state: ResearchState,
) -> str:
    """
    Decide whether to use previous research
    or perform a new search.
    """

    if state["use_memory"]:
        return "generate"

    return "planner"
