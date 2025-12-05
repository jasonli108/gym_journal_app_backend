import pytest
from fastapi.testclient import TestClient
from tinydb import TinyDB, Query
import os
import sys
from uuid import UUID, uuid4

# Add the project root and src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from main import app, get_db, get_password_hash
from models import WorkoutPlanBase, WorkoutPlanSummary, WorkoutPlanScheduleBase, WorkoutPlanScheduleDay, UserInDB
from enums import MuscleGroup, Exercise

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
    hashed_password = get_password_hash(user_data["password"])
    
    user_in_db = {"username": user_data["username"], "hashed_password": hashed_password}
    users_table.insert(user_in_db)
    
    return user_data

def get_auth_token(client: TestClient, username: str, password: str) -> str:
    """Helper to authenticate and retrieve an access token."""
    response = client.post("/token", data={"username": username, "password": password})
    assert response.status_code == 200
    return response.json()["access_token"]

def get_work_plan_data(user_id: str, name: str = "Test Plan", goal: str = "Test Goal", workplan_id: str = None):
    data = {
        "user_id": user_id,
        "name": name,
        "workoutplan_summary": {
            "goal": goal,
            "workout_type": "Full Body",
            "training_level": "Beginner",
            "program_duration": "4 Weeks",
            "days_per_week": 3,
            "time_per_workout": "60 Mins",
            "equipments": ["Dumbbell"],
            "target_gender": "Any",
            "recommended_supplements": ["None"]
        },
        "workoutplan_schedule": {
            "workoutplanScheduleId": str(uuid4()),
            "Monday": [
                {
                    "muscle_group": ["Chest"],
                    "exercise": ["BENCH_PRESS"]
                }
            ]
        }
    }
    if workplan_id:
        data["workplan_id"] = workplan_id
    return data

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
        "name": "Test Simple Plan",
                    "workoutplan_summary": {
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
                    "workoutplan_schedule": {
                        "workoutplanScheduleId": str(uuid4()),
                        "Monday": [
                            {
                                "muscle_group": ["Chest"],
                                "exercise": ["BENCH_PRESS"]
                            }
                        ]
                    }
                }
    # 3. Create the work plan
    response = client.post("/workoutplans/", json=work_plan_data, headers=headers)

    # 4. Assert creation was successful
    assert response.status_code == 200

def test_create_workplan_via_put(client):
    user_data = {"username": "putuser", "password": "password123"}
    client.post("/register/", json=user_data)
    token = get_auth_token(client, "putuser", "password123")
    headers = {"Authorization": f"Bearer {token}"}

    new_workplan_id = str(uuid4())
    work_plan_data = get_work_plan_data("putuser", name="New Plan via PUT", goal="New Goal via PUT", workplan_id=new_workplan_id)

    response = client.put(f"/workoutplans/{new_workplan_id}", json=work_plan_data, headers=headers)
    assert response.status_code == 200
    created_workplan = response.json()
    assert created_workplan["user_id"] == "putuser"
    assert created_workplan["name"] == "New Plan via PUT"
    assert created_workplan["workoutplan_summary"]["goal"] == "New Goal via PUT"
    assert "workoutplanScheduleId" in created_workplan["workoutplan_schedule"]
    assert created_workplan["workoutplan_id"] == new_workplan_id

def test_update_existing_workplan_via_put(client):
    user_data = {"username": "updateuser", "password": "password123"}
    client.post("/register/", json=user_data)
    token = get_auth_token(client, "updateuser", "password123")
    headers = {"Authorization": f"Bearer {token}"}

    # Create an initial workplan via POST
    initial_workplan_id = str(uuid4())
    initial_work_plan_data = get_work_plan_data("updateuser", name="Initial Plan", goal="Initial Goal", workplan_id=initial_workplan_id)
    response = client.post("/workoutplans/", json=initial_work_plan_data, headers=headers)
    assert response.status_code == 200
    
    # Update the existing workplan via PUT
    updated_goal = "Updated Goal via PUT"
    updated_name = "Updated Plan Name"
    updated_work_plan_data = get_work_plan_data("updateuser", name=updated_name, goal=updated_goal, workplan_id=initial_workplan_id)
    response = client.put(f"/workoutplans/{initial_workplan_id}", json=updated_work_plan_data, headers=headers)
    assert response.status_code == 200
    updated_workplan = response.json()
    assert updated_workplan["user_id"] == "updateuser"
    assert updated_workplan["name"] == updated_name
    assert updated_workplan["workoutplan_summary"]["goal"] == updated_goal
    assert "workoutplanScheduleId" in updated_workplan["workoutplan_schedule"]
    assert updated_workplan["workoutplan_id"] == initial_workplan_id

def test_update_workplan_forbidden_another_user(client):
    # Register user1 and create a workplan
    user1_data = {"username": "user1", "password": "password123"}
    client.post("/register/", json=user1_data)
    token1 = get_auth_token(client, "user1", "password123")
    headers1 = {"Authorization": f"Bearer {token1}"}

    workplan_id = str(uuid4())
    work_plan_data = get_work_plan_data("user1", name="User1's Plan", goal="User1's Goal", workplan_id=workplan_id)
    client.post("/workoutplans/", json=work_plan_data, headers=headers1)

    # Register user2
    user2_data = {"username": "user2", "password": "password123"}
    client.post("/register/", json=user2_data)
    token2 = get_auth_token(client, "user2", "password123")
    headers2 = {"Authorization": f"Bearer {token2}"}

    # User2 tries to update User1's workplan
    work_plan_data_for_user2 = get_work_plan_data("user1", name="User2 trying to update", goal="User2's Goal", workplan_id=workplan_id) # Still user1's plan
    response = client.put(f"/workoutplans/{workplan_id}", json=work_plan_data_for_user2, headers=headers2)
    assert response.status_code == 403
    assert response.json()["detail"] == "You can only create/update a workout plan for your own user."

    # User2 tries to create a plan for user1 via PUT
    new_workplan_id_for_user1 = str(uuid4())
    work_plan_data_for_user2_create = get_work_plan_data("user1", name="User2 trying to create for user1", goal="User2's Goal", workplan_id=new_workplan_id_for_user1)
    response = client.put(f"/workoutplans/{new_workplan_id_for_user1}", json=work_plan_data_for_user2_create, headers=headers2)
    assert response.status_code == 403
    assert response.json()["detail"] == "You can only create/update a workout plan for your own user."