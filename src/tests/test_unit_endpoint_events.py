import pytest
import httpx
from src.events.config import settings


def test_index(test_app):
    client = test_app.test_client()
    response = client.get("/api/events")
    assert response.status_code == 200
