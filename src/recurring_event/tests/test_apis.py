from fastapi.testclient import TestClient

from src.recurring_event.models import RecurringEvent
from src.server import app

client = TestClient(app)


def test_create_event():
    event = RecurringEvent(title="test", start="2021-01-01")
    event.flush()
    assert True
