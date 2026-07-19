from app.graph.state import ResearchState


def clarification_router(
    state: ResearchState,
) -> str:
    """
    Route the workflow after report evaluation.

    Workflow:

    Score >= 8
        -> Approved

    Score < 8
        -> Improve report

    After 2 improvement attempts
        -> Approve the latest version to avoid infinite loops.

    The clarification node is reserved for future interactive
    user conversations and is currently not used.
    """

    score = state.get("score", 0)
    attempts = state.get("attempts", 0)

    # High-quality report
    if score >= 8:
        return "approved"

    # Prevent infinite rewrite loops
    if attempts >= 2:
        return "approved"

    # Continue improving the report
    return "improve"