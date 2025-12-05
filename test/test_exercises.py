import pytest
from fastapi.testclient import TestClient
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from main import app
from enums import MuscleGroup

@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c

def test_get_all_exercises(client: TestClient):
    response = client.get("/exercises/")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_get_exercises_by_muscle_group(client: TestClient):
    response = client.get(f"/exercises/?muscle_group={MuscleGroup.CHEST.value}")
    assert response.status_code == 200
    exercises = response.json()
    assert len(exercises) > 0
    for exercise in exercises:
        assert exercise["muscle_group"] == MuscleGroup.CHEST.value

def test_get_exercises_by_multiple_filters(client: TestClient):
    response = client.get(f"/exercises/?muscle_group={MuscleGroup.LOWER_BACK.value}&is_popular=true")
    assert response.status_code == 200
    exercises = response.json()
    assert len(exercises) > 0
    for exercise in exercises:
        assert exercise["muscle_group"] == MuscleGroup.LOWER_BACK.value
        assert exercise["is_popular"] is True

def test_get_exercises_no_results(client: TestClient):
    response = client.get(f"/exercises/?muscle_group=Abs&mechanics_type=Isolation&is_popular=true")
    assert response.status_code == 200
    assert response.json() == []

