from abc import ABC, abstractmethod


class BaseLLM(ABC):
    """
    Abstract base class for all LLM providers.

    Every provider (OpenAI, Gemini, Anthropic, Ollama, etc.)
    must implement this interface.
    """

    @abstractmethod
    async def generate(
        self,
        prompt: str,
        system_prompt: str | None = None,
    ) -> str:
        """
        Generate a response from the language model.
        """
        pass

    @abstractmethod
    async def health_check(self) -> bool:
        """
        Verify that the provider is reachable and configured.
        """
        pass
