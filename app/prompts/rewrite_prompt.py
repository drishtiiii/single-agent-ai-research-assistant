def build_rewrite_prompt(
    report: str,
    feedback: str,
) -> str:
    return f"""
You are an expert researcher.

Improve the following report using the evaluation feedback.

Evaluation Feedback:

{feedback}

Original Report:

{report}

Return only the improved report.
"""
