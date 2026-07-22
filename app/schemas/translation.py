from pydantic import BaseModel


class TranslationRequest(BaseModel):
    report: str
    language: str