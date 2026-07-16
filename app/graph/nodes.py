from app.graph.state import ResearchState
from app.tools.search import SearchTool
from app.prompts.research_prompt import build_research_prompt
from app.services.llm_service import LLMService


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