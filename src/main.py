"""
main.py — Entry point for the research + summary agent.

Run with: python src/main.py
"""

from dotenv import load_dotenv
from src.graph.graph import build_graph

load_dotenv()


def main():
    graph = build_graph()

    # TODO: Replace with your actual query
    query = "What are the key principles of multi-agent AI systems?"

    print(f"Query: {query}\n")
    print("Running graph...\n")

    # TODO: Update invocation once state schema is defined
    # result = graph.invoke({"query": query})
    # print(result["summary"])


if __name__ == "__main__":
    main()
