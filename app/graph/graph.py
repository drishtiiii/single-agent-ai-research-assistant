from langgraph.graph import (
    END,
    START,
    StateGraph,
)

from app.graph.clarification_router import clarification_router
from app.graph.memory_router import memory_router
from app.graph.nodes import (
    clarification_node,
    database_node,
    evaluate_report_node,
    generate_report_node,
    improve_report_node,
    memory_node,
    planner_node,
    search_node,
)
from app.graph.planner_router import (
    planner_router,
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

builder.add_node(
    "database",
    database_node,
)
builder.add_node(
    "memory",
    memory_node,
)
builder.add_node(
    "clarification",
    clarification_node,
)


# -----------------------------
# Flow
# -----------------------------
builder.add_edge(
    START,
    "memory",
)

builder.add_conditional_edges(
    "memory",
    memory_router,
    {
        "planner": "planner",
        "generate": "generate",
    },
)

builder.add_conditional_edges(
    "planner",
    planner_router,
    {
        "search": "search",
        "database": "database",
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
    clarification_router,
    {
        "clarification": "clarification",
        "improve": "improve",
        "approved": END,
    },
)

builder.add_edge(
    "improve",
    "evaluate",
)
builder.add_edge(
    "database",
    "generate",
)
builder.add_edge(
    "clarification",
    END,
)
research_graph = builder.compile()
