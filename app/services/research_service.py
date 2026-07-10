from app.core.logger import logger
from app.exports.markdown_exporter import MarkdownExporter
from app.services.llm_service import LLMService
from app.tools.search import SearchTool


class ResearchService:
    """
    Service responsible for performing AI-powered research.
    """

    def __init__(self) -> None:
        self.search = SearchTool()
        self.llm = LLMService()
        self.exporter = MarkdownExporter()

        logger.info("Research Service initialized.")

    async def research(
        self,
        query: str,
    ) -> str:
        """
        Perform web research and generate a comprehensive answer.
        """

        logger.info(f"Research started for: {query}")

        # Search the web
        search_results = self.search.search(
            query=query,
            max_results=5,
        )

        # Build search context
        context = ""

        for index, result in enumerate(search_results, start=1):
            context += (
                f"\nResult {index}\n"
                f"Title: {result['title']}\n"
                f"URL: {result['url']}\n"
                f"Content: {result['body']}\n"
            )

        # Build the LLM prompt
        prompt = f"""
You are an expert AI Research Assistant.

Answer the user's question using ONLY the web search results below.

User Question:
{query}

Search Results:
{context}

Write a professional research report with:

1. Executive Summary
2. Key Findings
3. Detailed Explanation
4. Conclusion

If relevant, reference the source URLs naturally in your answer.
"""

        logger.info("Generating research report...")

        response = await self.llm.generate_response(
            prompt=prompt,
        )

        # Append sources
        sources = "\n\n---\n\n## Sources\n\n"

        for index, result in enumerate(search_results, start=1):
            sources += (
                f"{index}. {result['title']}\n"
                f"{result['url']}\n\n"
            )
        final_report = response + sources
        self.exporter.export(
            title=query,
            report=final_report,
        ) 

        logger.info("Research completed.")

        return final_report

        return response + sources