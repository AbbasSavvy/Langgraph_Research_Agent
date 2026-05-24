"""
state.py — Shared state schema for the research + summary graph.

Every node reads from this state and writes back to it.
This is the "shared memory" between the Researcher and Writer agents.

TODO: Define fields as you work through the conceptual design.
"""

from typing import Annotated
from langgraph.graph.message import add_messages
from typing_extensions import TypedDict


class ResearchState(TypedDict):
    # TODO: Add your state fields here
    # Hints: What does the Researcher need to pass to the Writer?
    # What does the graph need to track during the ReAct loop?
    pass
