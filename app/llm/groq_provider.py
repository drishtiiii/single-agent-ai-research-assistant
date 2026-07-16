from groq import Groq

from app.core.config import settings
from app.core.logger import logger
from app.llm.base import BaseLLM


class GroqProvider(BaseLLM):
    """
    Groq implementation of BaseLLM.
    """

    def __init__(self) -> None:
        self.client = Groq(
            api_key=settings.GROQ_API_KEY,
        )

        self.model = settings.LLM_MODEL

        logger.info(f"Initialized Groq provider with model: {self.model}")

    async def generate(
        self,
        prompt: str,
        system_prompt: str | None = None,
    ) -> str:

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

        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=settings.LLM_TEMPERATURE,
            max_tokens=settings.LLM_MAX_TOKENS,
        )

        return response.choices[0].message.content

    async def health_check(self) -> bool:
        try:
            self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "user",
                        "content": "Hello",
                    }
                ],
                max_tokens=settings.LLM_MAX_TOKENS,
            )
            return True

        except Exception as exc:
            logger.error(f"Groq health check failed: {exc}")
            return False
