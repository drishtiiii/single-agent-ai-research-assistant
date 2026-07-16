def build_evaluation_prompt(report: str) -> str:
    return f"""
You are an expert research evaluator.

Evaluate the following research report.

Score it from 1 to 10.

Return ONLY in this format:

Score: <number>

Feedback: <one paragraph>

Research Report:

{report}
"""
