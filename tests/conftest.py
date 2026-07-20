from unittest.mock import AsyncMock, patch

import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture(autouse=True)
def mock_background_task():
    """
    Prevent the background research task from
    calling the real LLM during tests.
    """
    with patch(
        "app.api.routes.research.run_research",
        new=AsyncMock(),
    ):
        yield


client = TestClient(app)
