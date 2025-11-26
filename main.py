from datetime import date
from typing import List, Dict, Optional
from uuid import UUID

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from tinydb import TinyDB, Query
from passlib.context import CryptContext

from .models import (
    WorkoutSession, WorkoutSessionIn, ExerciseOut,
    User, UserInDB, Token, UserCreate
)
from .enums import (
    Exercise, 
    MuscleGroup, 
    EquipmentType, 
    MechanicsType, 
    MyCustomGroup
)

# --- App and DB Initialization ---
app = FastAPI()

# Database Setup
db = TinyDB('backend/db.json')
workouts_table = db.table('workouts')
users_table = db.table('users')
UserQuery = Query()

# --- Security and Authentication Setup ---
# Password Hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# OAuth2 Scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# --- Security Helper Functions ---
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str):
    """Hashes the password, truncating to 72 bytes for bcrypt compatibility."""
    return pwd_context.hash(password.encode('utf-8')[:72])

def get_user(username: str):
    user = users_table.get(UserQuery.username == username)
    if user:
        return UserInDB(**user)

async def get_current_user(token: str = Depends(oauth2_scheme)):
    # For a simple prototype, we'll just check if the token is a valid username.
    # In a real app, you would decode a JWT here.
    user = get_user(username=token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

# --- API Endpoints ---
@app.get("/")
async def read_root():
    return {"message": "Welcome to the Gym Journal API! Visit /docs for documentation."}

# --- Auth Endpoints ---
@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = get_user(form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # For simplicity, we'll use the username as the token. A real app should use JWT.
    access_token = user.username
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/register/", response_model=User)
async def register_user(user_in: UserCreate):
    if get_user(user_in.username):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered"
        )
    hashed_password = get_password_hash(user_in.password)
    user_db = UserInDB(username=user_in.username, hashed_password=hashed_password)
    users_table.insert(user_db.dict())
    return User(username=user_in.username)

@app.get("/users/me/", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

# --- Workout Endpoints ---
@app.post("/workouts/", response_model=WorkoutSession)
async def create_workout_session(session_in: WorkoutSessionIn):
    new_session = WorkoutSession(**session_in.dict())
    # In a real app, you'd get user_id from the token, not the request body
    workouts_table.insert(new_session.dict(exclude={'session_id'}) | {'session_id': str(new_session.session_id)})
    return new_session

@app.get("/users/{user_id}/workouts/", response_model=List[WorkoutSession])
async def get_user_workouts(user_id: str, session_date: Optional[date] = None):
    query = (UserQuery.user_id == user_id)
    if session_date:
        query = query & (UserQuery.session_date == str(session_date))
    results = workouts_table.search(query)
    return results

# --- Exercise Endpoints ---
@app.get("/exercises/", response_model=List[ExerciseOut])
async def get_exercises(
    muscle_group: Optional[MuscleGroup] = None,
    equipment_type: Optional[EquipmentType] = None,
    mechanics_type: Optional[MechanicsType] = None,
    my_custom_group: Optional[MyCustomGroup] = None,
    is_popular: Optional[bool] = None
):
    all_exercises = []
    for member in Exercise:
        if (muscle_group and member.muscle_group != muscle_group) or \
           (equipment_type and member.equipment_type != equipment_type) or \
           (mechanics_type and member.mechanics_type != mechanics_type) or \
           (my_custom_group and member.my_custom_group != my_custom_group) or \
           (is_popular is not None and member.is_popular != is_popular):
            continue
        # This part has a bug in the original implementation, member.value is a tuple
        # A proper conversion is needed.
        exercise_data = ExerciseOut(
            id=member.name,
            display_name=member.value[0],
            muscle_group=member.value[1],
            url=member.value[2],
            is_popular=member.value[3],
            equipment_type=member.value[4],
            mechanics_type=member.value[5],
            my_custom_group=member.value[6],
        )
        all_exercises.append(exercise_data)
    return all_exercises
