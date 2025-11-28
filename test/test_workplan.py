import pytest
from fastapi.testclient import TestClient
from tinydb import TinyDB, Query
import os
import sys
from uuid import uuid4

# Add the project root and src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from src.main import app, get_db
from src.models import WorkPlanBase, WorkPlanSummary, WorkPlanScheduleBase, WorkPlanScheduleDay, UserInDB
from src.enums import MuscleGroup, Exercise

# --- Test Setup and Fixtures ---

# Use a separate test database
TEST_DB_PATH = "test_db.json"

@pytest.fixture
def test_db():
    """Fixture to set up and tear down a test database."""
    db = TinyDB(TEST_DB_PATH)
    yield db
    db.close()
    if os.path.exists(TEST_DB_PATH):
        os.remove(TEST_DB_PATH)

@pytest.fixture
def client(test_db):
    """Fixture to provide a test client for the FastAPI app with the overridden DB."""
    app.dependency_overrides[get_db] = lambda: test_db
    with TestClient(app) as c:
        yield c

# --- Helper Functions ---

def create_user_for_testing(client: TestClient, db: TinyDB, user_data: dict):
    """Helper to register a user and return the user data."""
    users_table = db.table('users')
    UserQuery = Query()
    
    # Use a hashed password for consistency with the main app
    from src.main import get_password_hash
    hashed_password = get_password_hash(user_data["password"])
    
    user_in_db = {"username": user_data["username"], "hashed_password": hashed_password}
    users_table.insert(user_in_db)
    
    return user_data

def get_auth_token(client: TestClient, username: str, password: str) -> str:
    """Helper to authenticate and retrieve an access token."""
    response = client.post("/token", data={"username": username, "password": password})
    assert response.status_code == 200
    return response.json()["access_token"]

# --- Test Cases ---

def test_create_workplan_simple(client):
    # 1. Register a user and get a token
    user_data = {"username": "testuser_simple", "password": "password123"}
    client.post("/register/", json=user_data)
    response = client.post("/token", data={"username": "testuser_simple", "password": "password123"})
    token = response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # 2. Define the work plan data
    work_plan_data = {
        "user_id": "testuser_simple",
        "workplan_summary": {
            "goal": "Test Goal",
            "workout_type": "Full Body",
            "training_level": "Beginner",
            "program_duration": "4 Weeks",
            "days_per_week": 3,
            "time_per_workout": "60 Mins",
            "equipments": ["Dumbbell"],
            "target_gender": "Any",
            "recommended_supplements": ["None"]
        },
        "workplan_schedule": {
            "id": "test_schedule",
            "monday": [
                {
                    "muscle_group": ["CHEST"],
                    "exercise": ["BENCH_PRESS"]
                }
            ]
        }
    }

    # 3. Create the work plan
    response = client.post("/workplans/", json=work_plan_data, headers=headers)

    # 4. Assert creation was successful
    assert response.status_code == 200