"""
researcher.py — Researcher agent node.

This agent runs the ReAct loop: it reasons about what to search,
calls the search tool, observes the result, and repeats until
it has enough information to hand off to the Writer.

TODO: Implement after covering the ReAct loop in depth.
"""


def researcher_node(state):
    # TODO: Implement the researcher agent
    # Steps:
    # 1. Build an LLM with the search tool bound to it
    # 2. Call the LLM with the current state messages
    # 3. Return updated state (the LLM response gets added to messages)
    pass
