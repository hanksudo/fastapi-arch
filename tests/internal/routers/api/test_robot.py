import pytest
from fastapi.testclient import TestClient
from collections.abc import Generator
from app.main import app

@pytest.fixture
def client() -> Generator[TestClient, None, None]:
    yield TestClient(app)

def test_get_list(client: TestClient) -> None:
    response = client.get("/robots")
    assert response.status_code == 200
    assert response.json() == [{'id': 1, 'name': 'R2D2'}]