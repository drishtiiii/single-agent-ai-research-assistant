from app.llm.base import BaseLLM
from app.llm.groq_provider import GroqProvider


class LLMFactory:
    """
    Factory responsible for creating the configured LLM.
    """

    @staticmethod
    def create() -> BaseLLM:
        return GroqProvider()
