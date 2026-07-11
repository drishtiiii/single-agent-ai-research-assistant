def build_research_prompt(
    query: str,
    context: str,
) -> str:
    """
    Build the research prompt for the LLM.
    """

    return f"""
You are an expert AI Research Assistant.

Your job is to create a professional, well-structured research report using ONLY the provided search results.

User Question:
{query}

Search Results:
{context}

Instructions:

- Do not invent facts.
- Base every statement on the provided search results.
- Write in a professional tone.
- Use clear headings.
- Keep the report factual and unbiased.

The report must contain:

# Executive Summary

A concise overview.

# Key Findings

Use bullet points.

# Detailed Explanation

Explain the topic thoroughly.

# Conclusion

Summarize the findings.

If relevant, naturally reference the source URLs in your explanation.
"""