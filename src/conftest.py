import pytest
from pony.orm import Database


@pytest.fixture(scope="session", autouse=True)
def initialize_test_db(request):
    db = Database()
    db.bind(provider="sqlite", filename=":memory:", create_db=True)
    db.generate_mapping(create_tables=True)
