from app.graph.state import ResearchState


def clarification_router(
    state: ResearchState,
) -> str:
    """
    Decide what happens after report evaluation.
    """

    # User clarification required
    if state["needs_input"]:
        return "clarification"

    # Report quality is good enough
    if state["score"] >= 8:
        return "approved"

    # Prevent infinite improvement loop
    if state["attempts"] >= 2:
        return "approved"

    # Improve report
    return "improve"