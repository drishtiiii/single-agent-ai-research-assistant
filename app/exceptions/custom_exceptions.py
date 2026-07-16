class ResearchNotFoundError(Exception):
    """
    Raised when a research report
    cannot be found.
    """

    def __init__(
        self,
        history_id: int,
    ):
        self.history_id = history_id

        super().__init__(f"Research report {history_id} not found.")


class ResearchGenerationError(Exception):
    """
    Raised when research generation fails.
    """

    pass
