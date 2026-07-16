import time


class Timer:
    """
    Simple execution timer.
    """

    def __init__(self):
        self.start = time.perf_counter()

    def elapsed(self) -> float:
        return round(
            time.perf_counter() - self.start,
            3,
        )
