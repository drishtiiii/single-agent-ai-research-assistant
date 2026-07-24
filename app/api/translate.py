from fastapi import APIRouter

from app.schemas.translation import TranslationRequest
from app.services.translator import TranslatorService

router = APIRouter(
    prefix="/translate",
    tags=["Translation"],
)

translator = TranslatorService()


@router.post("")
async def translate_report(
    request: TranslationRequest,
):
    translated = await translator.translate(
        report=request.report,
        language=request.language,
    )

    return {
        "success": True,
        "translated_report": translated,
    }
