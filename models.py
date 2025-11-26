from datetime import date
from typing import List, Optional
from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from .enums import (
    Exercise, 
    MuscleGroup, 
    EquipmentType, 
    MechanicsType, 
    MyCustomGroup
)

# --- Models for User and Authentication ---

class User(BaseModel):
    username: str

class UserCreate(User):
    password: str

class UserInDB(User):
    hashed_password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None


# --- Models for Workout Sessions ---

class ExerciseLog(BaseModel):
    exercise: Exercise
    sets: int
    reps: int
    weight_kg: Optional[float] = None

class WorkoutSessionIn(BaseModel):
    """The model for data coming from the user."""
    user_id: str
    session_date: date
    exercises: List[ExerciseLog]

class WorkoutSession(WorkoutSessionIn):
    """The model for data stored in our 'database'."""
    session_id: UUID = Field(default_factory=uuid4)


# --- Models for Exercise Listing ---

class ExerciseOut(BaseModel):
    """Defines the structure for returning an exercise from the API."""
    id: str  # The enum member name, e.g., "BENCH_PRESS"
    display_name: str
    muscle_group: MuscleGroup
    url: Optional[str]
    is_popular: bool
    equipment_type: Optional[EquipmentType]
    mechanics_type: Optional[MechanicsType]
    my_custom_group: Optional[MyCustomGroup]