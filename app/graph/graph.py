from langgraph.graph import (
    END,
    START,
    StateGraph,
)

from app.graph.nodes import (
    evaluate_report_node,
    generate_report_node,
    improve_report_node,
    planner_node,
    search_node,
)
from app.graph.planner_router import (
    planner_router,
)
from app.graph.router import (
    evaluation_router,
)
from app.graph.state import ResearchState

builder = StateGraph(
    ResearchState,
)

# -----------------------------
# Nodes
# -----------------------------
builder.add_node(
    "planner",
    planner_node,
)

builder.add_node(
    "search",
    search_node,
)

builder.add_node(
    "generate",
    generate_report_node,
)

builder.add_node(
    "evaluate",
    evaluate_report_node,
)

builder.add_node(
    "improve",
    improve_report_node,
)

# -----------------------------
# Flow
# -----------------------------
builder.add_edge(
    START,
    "planner",
)

builder.add_conditional_edges(
    "planner",
    planner_router,
    {
        "search": "search",
        "database": "generate",
        "calculator": "generate",
    },
)

builder.add_edge(
    "search",
    "generate",
)

builder.add_edge(
    "generate",
    "evaluate",
)

builder.add_conditional_edges(
    "evaluate",
    evaluation_router,
    {
        "accept": END,
        "improve": "improve",
    },
)

builder.add_edge(
    "improve",
    "evaluate",
)

research_graph = builder.compile()
