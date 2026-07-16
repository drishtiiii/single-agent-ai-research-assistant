from app.graph.state import ResearchState


def planner_router(
    state: ResearchState,
):

    tool = state["tool"]

    if tool == "DATABASE":
        return "database"

    if tool == "CALCULATOR":
        return "calculator"

    return "search"
