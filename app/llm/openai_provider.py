from openai import AsyncOpenAI

from app.core.config import settings
from app.core.logger import logger
from app.llm.base import BaseLLM


class OpenAIProvider(BaseLLM):
    """
    OpenAI implementation of the BaseLLM interface.
    """

    def __init__(self) -> None:
        self.client = AsyncOpenAI(
            api_key=settings.OPENAI_API_KEY,
            timeout=settings.REQUEST_TIMEOUT,
            max_retries=settings.MAX_RETRIES,
        )

        self.model = settings.LLM_MODEL
        self.temperature = settings.LLM_TEMPERATURE
        self.max_tokens = settings.LLM_MAX_TOKENS

        logger.info(f"Initialized OpenAI provider with model: {self.model}")

    async def generate(
        self,
        prompt: str,
        system_prompt: str | None = None,
    ) -> str:
        """
        Generate a response using the configured OpenAI model.
        """

        messages = []

        if system_prompt:
            messages.append(
                {
                    "role": "system",
                    "content": system_prompt,
                }
            )

        messages.append(
            {
                "role": "user",
                "content": prompt,
            }
        )

        response = await self.client.chat.completions.create(
            model=self.model,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            messages=messages,
        )

        return response.choices[0].message.content or ""

    async def health_check(self) -> bool:
        """
        Verify connectivity to the OpenAI API.
        """

        try:
            await self.client.models.list()
            return True
        except Exception as exc:
            logger.error(f"OpenAI health check failed: {exc}")
            return False
