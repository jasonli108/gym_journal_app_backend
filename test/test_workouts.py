import pytest
from fastapi.testclient import TestClient
from tinydb import TinyDB
import os
import sys
from datetime import date

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from src.main import app, get_db
from src.enums import Exercise

# --- Test Setup and Fixtures ---

TEST_DB_PATH = "test_db_workouts.json"

@pytest.fixture(scope="module")
def test_db():
    """Fixture to set up and tear down a test database for the module."""
    if os.path.exists(TEST_DB_PATH):
        os.remove(TEST_DB_PATH)
    db = TinyDB(TEST_DB_PATH)
    yield db
    db.close()
    if os.path.exists(TEST_DB_PATH):
        os.remove(TEST_DB_PATH)

@pytest.fixture(scope="module")
def client(test_db):
    """Fixture to provide a test client for the FastAPI app with the overridden DB."""
    app.dependency_overrides[get_db] = lambda: test_db
    with TestClient(app) as c:
        yield c

# --- Test Cases ---

def test_create_and_get_workout_session(client: TestClient):
    # 1. Register a user
    user_data = {"username": "workoutuser", "password": "password123"}
    client.post("/register/", json=user_data)

    # 2. Define workout session data
    session_data = {
        "user_id": "workoutuser",
        "session_date": str(date.today()),
        "exercises": [
            {
                "exercise": "Bench Press",
                "sets": 3,
                "reps": 12,
                "weight_kg": 100
            }
        ]
    }

    # 3. Create a workout session
    response = client.post("/workouts/", json=session_data)
    assert response.status_code == 200
    created_session = response.json()
    assert created_session["user_id"] == "workoutuser"
    assert created_session["exercises"][0]["exercise"] == "Bench Press"
    # 4. Get user's workouts
    response = client.get(f"/users/workoutuser/workouts/")
    assert response.status_code == 200
    workouts = response.json()
    assert len(workouts) == 1
    assert workouts[0]["user_id"] == "workoutuser"
    assert workouts[0]["exercises"][0]["exercise"] == "Bench Press"

    # 5. Get user's workouts for a specific date
    response = client.get(f"/users/workoutuser/workouts/?session_date={date.today()}")
    assert response.status_code == 200
    workouts = response.json()
    assert len(workouts) == 1

    # 6. Get user's workouts for a different date
    response = client.get(f"/users/workoutuser/workouts/?session_date=2023-01-01")
    assert response.status_code == 200
    workouts = response.json()
    assert len(workouts) == 0

    # 7. Get workouts for a non-existent user
    response = client.get("/users/nouser/workouts/")
    assert response.status_code == 200
    assert len(response.json()) == 0
