import pytest
from fastapi.testclient import TestClient
from tinydb import TinyDB, Query
import os
import sys

# Add the project root and src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from main import app, get_db

# --- Test Setup and Fixtures ---

# Use a separate test database
TEST_DB_PATH = "test_db_main.json"

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

def test_read_root(client: TestClient):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Gym Journal API! Visit /docs for documentation."}

def test_register_user(client: TestClient):
    user_data = {"username": "testuser", "password": "password123"}
    response = client.post("/register/", json=user_data)
    assert response.status_code == 200
    assert response.json() == {"username": "testuser"}

    # Test registering the same user again
    response = client.post("/register/", json=user_data)
    assert response.status_code == 400
    assert response.json() == {"detail": "Username already registered"}

def test_login_for_access_token(client: TestClient):
    # First, register a user
    user_data = {"username": "loginuser", "password": "password123"}
    client.post("/register/", json=user_data)
    
    # Test successful login
    login_data = {"username": "loginuser", "password": "password123"}
    response = client.post("/token", data=login_data)
    assert response.status_code == 200
    json_response = response.json()
    assert "access_token" in json_response
    assert json_response["token_type"] == "bearer"

    # Test incorrect password
    login_data["password"] = "wrongpassword"
    response = client.post("/token", data=login_data)
    assert response.status_code == 401
    assert response.json() == {"detail": "Incorrect username or password"}

    # Test incorrect username
    login_data["username"] = "wronguser"
    login_data["password"] = "password123"
    response = client.post("/token", data=login_data)
    assert response.status_code == 401
    assert response.json() == {"detail": "Incorrect username or password"}


def test_read_users_me(client: TestClient):
    # First, register and login
    user_data = {"username": "me_user", "password": "password123"}
    client.post("/register/", json=user_data)
    login_data = {"username": "me_user", "password": "password123"}
    response = client.post("/token", data=login_data)
    token = response.json()["access_token"]

    # Test /users/me/
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/users/me/", headers=headers)
    assert response.status_code == 200
    assert response.json() == {"username": "me_user"}

    # Test with invalid token
    headers = {"Authorization": "Bearer invalidtoken"}
    response = client.get("/users/me/", headers=headers)
    assert response.status_code == 401
    assert response.json() == {"detail": "Invalid authentication credentials"}