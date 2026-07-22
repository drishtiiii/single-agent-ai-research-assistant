from app.llm.factory import LLMFactory
from app.prompts.translation_prompt import build_translation_prompt


class TranslatorService:
    """
    Service for translating research reports.
    """

    def __init__(self):
        self.llm = LLMFactory.create()

    async def translate(
        self,
        report: str,
        language: str,
    ) -> str:
        """
        Translate a report into the requested language.
        """

        prompt = build_translation_prompt(
            report=report,
            language=language,
        )

        translated_report = await self.llm.generate(prompt)

        return translated_report.strip()