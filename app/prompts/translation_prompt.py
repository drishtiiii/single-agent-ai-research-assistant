def build_translation_prompt(
    report: str,
    language: str,
) -> str:
    """
    Build a translation prompt for the LLM.
    """

    return f"""
You are an expert professional translator.

Translate the following research report into **{language}**.

Requirements:

- Preserve all Markdown formatting.
- Preserve headings.
- Preserve bullet points.
- Preserve numbered lists.
- Preserve technical terminology.
- Do NOT summarize.
- Do NOT omit information.
- Do NOT add new information.
- Translate naturally and fluently.

Return ONLY the translated report.

Research Report:

{report}
"""
