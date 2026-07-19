import re

from app.core.logger import logger
from app.core.timer import Timer
from app.database.crud import find_previous_research
from app.database.database import SessionLocal
from app.graph.state import ResearchState
from app.prompts.evaluation_prompt import build_evaluation_prompt
from app.prompts.planner_prompt import build_planner_prompt
from app.prompts.research_prompt import build_research_prompt
from app.prompts.rewrite_prompt import build_rewrite_prompt
from app.services.llm_service import LLMService
from app.tools.search import SearchTool
from app.tools.wikipedia import WikipediaTool


search_tool = SearchTool()
llm = LLMService()
wikipedia_tool = WikipediaTool()

async def memory_node(
    state: ResearchState,
):
    """
    Check whether similar research already exists.
    """

    logger.info(
        "[{}] Checking memory...",
        state["request_id"],
    )

    db = SessionLocal()

    try:
        previous = find_previous_research(
            db=db,
            query=state["query"],
        )

        if previous:
            logger.info(
                "[{}] Previous research found.",
                state["request_id"],
            )

            return {
                "context": previous.report,
                "use_memory": True,
            }

        logger.info(
            "[{}] No previous research found.",
            state["request_id"],
        )

        return {
            "use_memory": False,
        }

    finally:
        db.close()


async def planner_node(
    state: ResearchState,
):
    """
    Decide which tool should answer the query.
    """

    timer = Timer()
    request_id = state["request_id"]

    logger.info(
        "[{}] Planner node started.",
        request_id,
    )

    prompt = build_planner_prompt(
        query=state["query"],
    )

    tool = (
        (
            await llm.generate_response(
                prompt=prompt,
            )
        )
        .strip()
        .upper()
    )

    logger.info(
        "[{}] Planner selected tool: {}",
        request_id,
        tool,
    )

    logger.info(
        "[{}] Planner node completed in {:.3f} sec.",
        request_id,
        timer.elapsed(),
    )

    return {
        "tool": tool,
    }


def search_node(
    state: ResearchState,
):
    """
    Search DuckDuckGo and Wikipedia for relevant information.
    """

    timer = Timer()
    request_id = state["request_id"]

    logger.info(
        "[{}] Search node started.",
        request_id,
    )

    # -----------------------
    # DuckDuckGo Search
    # -----------------------

    results = search_tool.search(
        query=state["query"],
        max_results=3,
    )

    context = "# DuckDuckGo Results\n\n"

    for index, result in enumerate(results, start=1):

        context += (
            f"\nResult {index}\n"
            f"Title: {result['title']}\n"
            f"URL: {result['url']}\n"
            f"Content: {result['body']}\n"
        )

    # -----------------------
    # Wikipedia Search
    # -----------------------

    wiki_context = wikipedia_tool.search(
        state["query"]
    )

    if wiki_context:

        context += (
            "\n\n"
            "=====================================\n"
            "Wikipedia\n"
            "=====================================\n\n"
        )

        context += wiki_context

    logger.info(
        "[{}] Search node completed in {:.3f} sec.",
        request_id,
        timer.elapsed(),
    )

    return {
        "context": context,
    }

async def database_node(
    state: ResearchState,
):
    """
    Placeholder for future database retrieval.
    """

    timer = Timer()
    request_id = state["request_id"]

    logger.info(
        "[{}] Database node started.",
        request_id,
    )

    logger.info(
        "[{}] Database node completed in {:.3f} sec.",
        request_id,
        timer.elapsed(),
    )

    return {
        "context": "",
    }


async def generate_report_node(
    state: ResearchState,
):
    """
    Generate the research report.
    """

    timer = Timer()
    request_id = state["request_id"]

    logger.info(
        "[{}] Report generation started.",
        request_id,
    )

    prompt = build_research_prompt(
        query=state["query"],
        context=state["context"],
    )

    report = await llm.generate_response(
        prompt=prompt,
    )

    logger.info(
        "[{}] Report generation completed in {:.3f} sec.",
        request_id,
        timer.elapsed(),
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

    timer = Timer()
    request_id = state["request_id"]

    logger.info(
        "[{}] Evaluation node started.",
        request_id,
    )

    prompt = build_evaluation_prompt(
        report=state["report"],
    )

    evaluation = await llm.generate_response(
        prompt=prompt,
    )

    print("\n========== EVALUATION ==========")
    print(evaluation)
    print("================================\n")

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

    logger.info(
        "[{}] Evaluation score: {}",
        request_id,
        score,
    )

    logger.info(
        "[{}] Evaluation node completed in {:.3f} sec.",
        request_id,
        timer.elapsed(),
    )

    needs_input = score < 6
    return {
        "score": score,
        "feedback": feedback,
        "needs_input": needs_input,
    }


async def clarification_node(
    state: ResearchState,
):
    """
    Ask the user for clarification.
    """

    logger.info(
        "[{}] Clarification required.",
        state["request_id"],
    )

    return {
        "clarification": (
            "The research request is too broad or the "
            "generated report quality is insufficient. "
            "Please provide more specific details."
        ),
    }


async def improve_report_node(
    state: ResearchState,
):
    """
    Improve the report using evaluator feedback.
    """

    timer = Timer()
    request_id = state["request_id"]

    logger.info(
        "[{}] Improvement node started.",
        request_id,
    )

    prompt = build_rewrite_prompt(
        report=state["report"],
        feedback=state["feedback"],
    )

    improved_report = await llm.generate_response(
        prompt=prompt,
    )

    logger.info(
        "[{}] Improvement node completed in {:.3f} sec.",
        request_id,
        timer.elapsed(),
    )

    return {
        "report": improved_report,
        "attempts": state["attempts"] + 1,
    }
