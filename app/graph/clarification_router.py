from app.graph.state import ResearchState


def clarification_router(
    state: ResearchState,
) -> str:
    if state["needs_input"]:
        return "clarification"

    return "improve"
