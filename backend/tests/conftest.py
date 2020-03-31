import pytest

from api.app import app


@pytest.fixture
def backend_api_client(scope="method"):
    with app.test_client() as client:
        yield client
