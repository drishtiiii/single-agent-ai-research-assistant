from .conftest import client


def test_research_empty_query():

    response = client.post(
        "/research",
        json={"query": ""},
    )

    assert response.status_code == 422


def test_research_short_query():

    response = client.post(
        "/research",
        json={"query": "AI"},
    )

    assert response.status_code == 422


def test_research_success():

    response = client.post(
        "/research",
        json={"query": "Artificial Intelligence"},
    )

    assert response.status_code == 200

    data = response.json()

    assert data["success"] is True

    assert (
        data["report"]
        == "Research has started in the background. Please check your history shortly."
    )
