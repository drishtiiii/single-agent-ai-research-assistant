import re
from pathlib import Path

from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer

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

        Path(output_dir).mkdir(
            parents=True,
            exist_ok=True,
        )

        safe_title = title.strip().lower()

        safe_title = re.sub(
            r'[\\/*?:"<>|]',
            "",
            safe_title,
        )

        safe_title = safe_title.replace(" ", "_")

        safe_title = re.sub(
            r"_+",
            "_",
            safe_title,
        )

        safe_title = safe_title.strip("_")

        if not safe_title:
            safe_title = "research_report"

        filepath = Path(output_dir) / f"{safe_title}.pdf"

        doc = SimpleDocTemplate(
            str(filepath),
            leftMargin=40,
            rightMargin=40,
            topMargin=40,
            bottomMargin=40,
        )

        styles = getSampleStyleSheet()

        title_style = ParagraphStyle(
            "CustomTitle",
            parent=styles["Title"],
            alignment=TA_CENTER,
            spaceAfter=20,
        )

        body_style = ParagraphStyle(
            "Body",
            parent=styles["BodyText"],
            leading=22,
            spaceAfter=8,
        )

        story = []

        story.append(
            Paragraph(
                title,
                title_style,
            )
        )

        story.append(
            Spacer(
                1,
                20,
            )
        )

        for line in report.split("\n"):

            if line.strip():

                story.append(
                    Paragraph(
                        line,
                        body_style,
                    )
                )

            else:

                story.append(
                    Spacer(
                        1,
                        10,
                    )
                )

        doc.build(story)

        logger.info(
            "PDF report exported to {}",
            filepath,
        )

        return str(filepath)