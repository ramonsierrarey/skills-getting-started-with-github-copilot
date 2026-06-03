import copy

import pytest
from src.app import activities, app

_original_activities = copy.deepcopy(activities)


@pytest.fixture(autouse=True)
def reset_activities():
    """Reset in-memory activity data before each test."""
    activities.clear()
    activities.update(copy.deepcopy(_original_activities))
    yield


@pytest.fixture
def client():
    from fastapi.testclient import TestClient

    with TestClient(app) as test_client:
        yield test_client
