from ddgs import DDGS

from app.core.logger import logger


class SearchTool:
    """
    DuckDuckGo Search Tool using the official DDGS package.
    """

    def search(
        self,
        query: str,
        max_results: int = 5,
    ) -> list[dict]:

        logger.info(f"Searching for: {query}")

        results = []

        with DDGS() as ddgs:
            search_results = ddgs.text(
                query,
                max_results=max_results,
            )

            for item in search_results:
                results.append(
                    {
                        "title": item.get("title", ""),
                        "url": item.get("href", ""),
                        "body": item.get("body", ""),
                    }
                )

        logger.info(f"Found {len(results)} results.")

        return results
