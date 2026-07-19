import re
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

        # Create reports directory
        Path(output_dir).mkdir(
            parents=True,
            exist_ok=True,
        )

        # -------------------------
        # Create a safe filename
        # -------------------------
        safe_title = title.strip().lower()

        # Remove invalid filename characters
        safe_title = re.sub(
            r'[\\/*?:"<>|]',
            "",
            safe_title,
        )

        # Replace spaces with underscores
        safe_title = safe_title.replace(" ", "_")

        # Remove duplicate underscores
        safe_title = re.sub(
            r"_+",
            "_",
            safe_title,
        )

        # Remove leading/trailing underscores
        safe_title = safe_title.strip("_")

        # Fallback filename
        if not safe_title:
            safe_title = "research_report"

        filename = f"{safe_title}.pdf"

        filepath = Path(output_dir) / filename

        # -------------------------
        # Build PDF
        # -------------------------
        doc = SimpleDocTemplate(str(filepath))

        styles = getSampleStyleSheet()

        story = [
            Paragraph(title, styles["Title"]),
            Paragraph(
                report.replace("\n", "<br/>"),
                styles["BodyText"],
            ),
        ]

        doc.build(story)

        logger.info(
            "PDF report exported to {}",
            filepath,
        )

        return str(filepath)