def build_evaluation_prompt(report: str) -> str:
    return f"""
You are an expert AI Research Report evaluator.

Evaluate the report ONLY on the following criteria:

1. Accuracy of information
2. Completeness of the answer
3. Logical structure
4. Clarity and readability
5. Overall usefulness to a general user

DO NOT evaluate:
- originality
- novelty
- academic contribution
- research publication quality
- scholarly rigor

Scoring Guide:

10 = Excellent, comprehensive, accurate and well-organized.
9 = Very strong report with only minor improvements possible.
8 = Good report covering the topic well.
7 = Useful report with some missing details.
6 = Acceptable report that answers the question correctly.
5 = Basic report with noticeable shortcomings.
4 or below = Poor report or missing important information.

Return ONLY in this exact format:

Score: <number>

Feedback: <one concise paragraph describing improvements if needed>

Research Report:

{report}
"""