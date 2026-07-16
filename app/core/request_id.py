from uuid import uuid4


def generate_request_id() -> str:
    """
    Generate a short request ID for tracing logs.
    """

    return uuid4().hex[:8]
