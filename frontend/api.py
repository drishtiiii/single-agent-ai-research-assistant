import requests

from config import API_URL


def start_research(query: str):
    response = requests.post(
        f"{API_URL}/research",
        json={"query": query},
        timeout=10,
    )
    response.raise_for_status()
    return response.json()


def get_history():
    response = requests.get(
        f"{API_URL}/history",
        timeout=10,
    )
    response.raise_for_status()
    return response.json()


def get_report(history_id: int):
    response = requests.get(
        f"{API_URL}/history/{history_id}",
        timeout=10,
    )
    response.raise_for_status()
    return response.json()


def delete_report(history_id: int):
    response = requests.delete(
        f"{API_URL}/history/{history_id}",
        timeout=10,
    )
    response.raise_for_status()
    return response.json()


def get_markdown_file(history_id: int):
    response = requests.get(
        f"{API_URL}/history/{history_id}/download/markdown",
        timeout=60,
    )
    response.raise_for_status()
    return response.content


def get_pdf_file(history_id: int):
    response = requests.get(
        f"{API_URL}/history/{history_id}/download/pdf",
        timeout=60,
    )
    response.raise_for_status()
    return response.content