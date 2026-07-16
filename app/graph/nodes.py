import re

from app.core.logger import logger
from app.graph.state import ResearchState
from app.prompts.evaluation_prompt import (
    build_evaluation_prompt,
)
from app.prompts.planner_prompt import (
    build_planner_prompt,
)
from app.prompts.research_prompt import build_research_prompt
from app.prompts.rewrite_prompt import (
    build_rewrite_prompt,
)
from app.services.llm_service import LLMService
from app.tools.search import SearchTool

search_tool = SearchTool()
llm = LLMService()


def search_node(state: ResearchState):

    results = search_tool.search(
        query=state["query"],
        max_results=5,
    )

    context = ""

    for index, result in enumerate(results, start=1):
        context += (
            f"\nResult {index}\n"
            f"Title: {result['title']}\n"
            f"URL: {result['url']}\n"
            f"Content: {result['body']}\n"
        )

    return {
        "context": context,
    }


async def planner_node(
    state: ResearchState,
):
    """
    Decide which tool should be used.
    """

    prompt = build_planner_prompt(
        state["query"],
    )

    decision = await llm.generate_response(
        prompt=prompt,
    )

    tool = decision.strip().upper()

    logger.info(f"Planner selected: {tool}")

    return {
        "tool": tool,
    }


async def generate_report_node(
    state: ResearchState,
):

    prompt = build_research_prompt(
        query=state["query"],
        context=state["context"],
    )

    report = await llm.generate_response(
        prompt=prompt,
    )

    return {
        "report": report,
    }



async def evaluate_report_node(
    state: ResearchState,
):
    """
    Evaluate the quality of the generated report.
    """

    prompt = build_evaluation_prompt(
        report=state["report"],
    )

    evaluation = await llm.generate_response(
        prompt=prompt,
    )

    logger.info(f"Evaluation:\n{evaluation}")

    score = 5
    feedback = evaluation

    match = re.search(
        r"Score:\s*(\d+)",
        evaluation,
    )

    if match:
        score = int(match.group(1))

    feedback_match = re.search(
        r"Feedback:\s*(.*)",
        evaluation,
        re.DOTALL,
    )

    if feedback_match:
        feedback = feedback_match.group(1).strip()

    return {
        "score": score,
        "feedback": feedback,
    }


async def improve_report_node(
    state: ResearchState,
):
    """
    Improve the report using evaluator feedback.
    """

    prompt = build_rewrite_prompt(
        report=state["report"],
        feedback=state["feedback"],
    )

    improved_report = await llm.generate_response(
        prompt=prompt,
    )

    logger.info("Report improved.")

    return {
        "report": improved_report,
        "attempts": state["attempts"] + 1,
    }
