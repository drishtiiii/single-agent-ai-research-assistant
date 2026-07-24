from fastapi import APIRouter
from fastapi.responses import FileResponse

from app.exports.pdf_exporter import PDFExporter
from app.schemas.translation import TranslationRequest

router = APIRouter()


@router.post("/translate/pdf")
async def translate_pdf(
    request: TranslationRequest,
):

    exporter = PDFExporter()

    pdf_path = exporter.export(
        title=f"{request.language}_{request.report[:40]}",
        report=request.report,
    )

    return FileResponse(
        pdf_path,
        media_type="application/pdf",
        filename=pdf_path.split("/")[-1],
    )
