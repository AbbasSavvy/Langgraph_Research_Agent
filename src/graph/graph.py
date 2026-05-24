"""
graph.py — Graph definition: nodes, edges, and compilation.

This is where the LangGraph graph is assembled.
The flow is: START → Research Node ⇄ Tool Node → Write Node → END

TODO: Wire up nodes and edges after implementing agents and tools.
"""

from langgraph.graph import StateGraph, START, END
from src.graph.state import ResearchState


def build_graph():
    graph = StateGraph(ResearchState)

    # TODO: Add nodes
    # graph.add_node("researcher", ...)
    # graph.add_node("tools", ...)
    # graph.add_node("writer", ...)

    # TODO: Add edges
    # graph.add_edge(START, "researcher")
    # graph.add_conditional_edges("researcher", ...)
    # graph.add_edge("tools", "researcher")
    # graph.add_edge("writer", END)

    return graph.compile()
