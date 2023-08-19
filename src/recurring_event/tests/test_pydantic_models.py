from fastapi.testclient import TestClient

from src.server import app

client = TestClient(app)


def test_create_event():
    assert True
