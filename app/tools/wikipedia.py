import wikipedia

from app.core.logger import logger


class WikipediaTool:
    """
    Wikipedia search tool.
    """

    def search(
        self,
        query: str,
    ) -> str:

        try:

            wikipedia.set_lang("en")

            page = wikipedia.page(
                query,
                auto_suggest=True,
            )

            summary = wikipedia.summary(
                query,
                sentences=5,
            )

            logger.info(
                f"Wikipedia page found: {page.title}"
            )

            return f"""
Title:
{page.title}

Summary:
{summary}

URL:
{page.url}
"""

        except Exception as e:

            logger.warning(
                f"Wikipedia search failed: {e}"
            )

            return ""