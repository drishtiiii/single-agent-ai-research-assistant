def build_planner_prompt(
    query: str,
) -> str:
    return f"""
You are an AI planning agent.

Choose the BEST tool.

Available tools

SEARCH
DATABASE
CALCULATOR

Return ONLY one word.

Query:

{query}
"""
