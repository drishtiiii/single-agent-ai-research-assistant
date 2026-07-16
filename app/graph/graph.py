from langgraph.graph import START, END, StateGraph

from app.graph.state import ResearchState
from app.graph.nodes import (
    search_node,
    generate_report_node,
)

builder = StateGraph(
    ResearchState,
)

builder.add_node(
    "search",
    search_node,
)

builder.add_node(
    "generate",
    generate_report_node,
)

builder.add_edge(
    START,
    "search",
)

builder.add_edge(
    "search",
    "generate",
)

builder.add_edge(
    "generate",
    END,
)

research_graph = builder.compile()