import re
from pathlib import Path

from app.core.logger import logger


class MarkdownExporter:
    """
    Utility for exporting research reports as Markdown files.
    """

    def export(
        self,
        title: str,
        report: str,
        output_dir: str = "reports",
    ) -> str:
        """
        Export a research report to a Markdown file.

        Returns the path of the generated file.
        """

        # Create reports directory if it doesn't exist
        Path(output_dir).mkdir(
            parents=True,
            exist_ok=True,
        )

        # -------------------------
        # Create a safe filename
        # -------------------------
        safe_title = title.strip().lower()

        # Remove characters invalid on Windows/macOS/Linux
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

        filename = f"{safe_title}.md"

        filepath = Path(output_dir) / filename

        markdown = f"# {title}\n\n{report}\n"

        filepath.write_text(
            markdown,
            encoding="utf-8",
        )

        logger.info(
            "Markdown report exported to {}",
            filepath,
        )

        return str(filepath)
