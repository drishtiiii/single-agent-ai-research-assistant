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

        filename = f"{safe_title}.md"

        filepath = Path(output_dir) / filename

        markdown = (
            f"# {title}\n\n"
            f"{report}\n"
        )

        filepath.write_text(
            markdown,
            encoding="utf-8",
        )

        logger.info(
            f"Markdown report exported to {filepath}"
        )

        return str(filepath)