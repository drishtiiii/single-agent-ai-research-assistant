from app.core.logger import logger
from app.llm.base import BaseLLM
from app.llm.factory import LLMFactory


class LLMService:
    """
    Service layer responsible for interacting with the configured LLM.
    """

    def __init__(self, llm: BaseLLM | None = None) -> None:
        self.llm = llm or LLMFactory.create()

    async def generate_response(
        self,
        prompt: str,
        system_prompt: str | None = None,
    ) -> str:
        """
        Generate a response using the configured LLM.
        """

        logger.info("Generating LLM response...")

        response = await self.llm.generate(
            prompt=prompt,
            system_prompt=system_prompt,
        )

        logger.info("LLM response generated successfully.")

        return response

    async def health_check(self) -> bool:
        """
        Check whether the configured LLM provider is healthy.
        """
        return await self.llm.health_check()