from app.core.config import settings
from app.llm.base import BaseLLM
from app.llm.gemini_provider import GeminiProvider
from app.llm.openai_provider import OpenAIProvider


class LLMFactory:
    """
    Factory responsible for creating LLM providers.
    """

    @staticmethod
    def create() -> BaseLLM:
        provider = settings.LLM_PROVIDER.lower()

        if provider == "gemini":
            return GeminiProvider()

        if provider == "openai":
            return OpenAIProvider()

        raise ValueError(
            f"Unsupported LLM provider: {provider}"
        )