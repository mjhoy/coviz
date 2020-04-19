import os

import pytest

from api.app import app


@pytest.fixture
def backend_api_client(scope="method"):
    os.environ["FRONTEND_ADDRESS"] = "http://test.dev"
    with app.test_client() as client:
        yield client
