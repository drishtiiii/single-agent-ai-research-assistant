from pathlib import Path

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate

from app.core.logger import logger


class PDFExporter:
    """
    Utility for exporting research reports as PDF files.
    """

    def export(
        self,
        title: str,
        report: str,
        output_dir: str = "reports",
    ) -> str:
        """
        Export a research report to a PDF file.

        Returns the path of the generated file.
        """

        Path(output_dir).mkdir(
            parents=True,
            exist_ok=True,
        )

        safe_title = (
            title.lower()
            .replace(" ", "_")
            .replace("/", "_")
            .replace("\\", "_")
        )

        filename = f"{safe_title}.pdf"

        filepath = Path(output_dir) / filename

        doc = SimpleDocTemplate(str(filepath))

        styles = getSampleStyleSheet()

        story = []

        story.append(
            Paragraph(f"<b>{title}</b>", styles["Title"])
        )

        story.append(
            Paragraph(report.replace("\n", "<br/>"), styles["BodyText"])
        )

        doc.build(story)

        logger.info(
            f"PDF report exported to {filepath}"
        )

        return str(filepath)