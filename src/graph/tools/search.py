"""
search.py — Mock search tool for the Researcher agent.

A tool is defined by three things: name, description, and parameters.
The LLM picks tools based on their description — so be specific.

We use a mock tool to start so we can focus on graph mechanics
without worrying about API keys or rate limits.

TODO: Replace mock with a real search API (e.g. Tavily) later.
"""

from langchain_core.tools import tool


@tool
def search(query: str) -> str:
    """
    Search the web for information about a given topic.
    Use this to gather facts, recent events, or background knowledge.
    """
    # TODO: Replace with a real search call (e.g. Tavily, SerpAPI)
    # For now, returns a placeholder so the graph flow can be tested
    return f"[Mock result for: '{query}'] — Replace this with a real search tool."
