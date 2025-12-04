from datetime import date
from typing import List, Optional
from pydantic import BaseModel, Field, model_validator, validator
from uuid import UUID, uuid4
from backend.src.enums import MuscleGroup, EquipmentType, MechanicsType, MyCustomGroup
from backend.src.exercises.all_exercises import get_exercise_by_display_name
from backend.src.exercises.main import Exercise

from pydantic import BaseModel, Field, model_validator, validator

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
    exercise: Exercise  # Type hint remains Exercise for internal use
    sets: Optional[int] = None
    reps: Optional[int] = None
    weight_kg: Optional[int] = None

    @validator("exercise", pre=True)
    def convert_exercise_name_to_enum(cls, v):
        if isinstance(v, str):
            try:
                return get_exercise_by_display_name(v)
            except ValueError as e:
                raise ValueError(f"Invalid exercise name: {v}") from e
        return v


class WorkoutSessionIn(BaseModel):
    """The model for data coming from the user."""

    user_id: str
    session_date: date
    exercises: List[ExerciseLog]


class WorkoutSession(WorkoutSessionIn):
    """The model for data stored in our 'database'."""

    session_id: UUID = Field(default_factory=uuid4)


class ExerciseLogOut(BaseModel):
    exercise: str
    sets: Optional[int] = None
    reps: Optional[int] = None
    weight_kg: Optional[int] = None


class WorkoutSessionOut(BaseModel):
    """The model for data sent to the user."""

    session_id: UUID
    user_id: str
    session_date: date
    exercises: List[ExerciseLogOut]


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


class WorkoutPlanScheduleDay(BaseModel):
    muscle_group: List[MuscleGroup]
    exercise: List[Exercise]

    @model_validator(mode="before")
    @classmethod
    def clean_empty_exercises(cls, data):
        if isinstance(data, dict) and "exercise" in data and isinstance(data["exercise"], list):
            data["exercise"] = [ex for ex in data["exercise"] if ex]
        return data

    @validator("muscle_group", pre=True, each_item=True)
    def convert_muscle_group_name_to_enum(cls, v):
        if isinstance(v, str):
            try:
                return MuscleGroup(v)  # Look up by value
            except ValueError as e:
                raise ValueError(f"Invalid MuscleGroup name: {v}") from e
        return v

    @validator("exercise", pre=True, each_item=True)
    def convert_exercise_name_to_enum(cls, v):
        if isinstance(v, str):
            # Handle string representations (e.g., from API requests)
            try:
                # First try looking up by enum member name (e.g., "BENCH_PRESS")
                return Exercise[v]
            except KeyError:
                try:
                    # Then try looking up by display name (e.g., "Bench Press")
                    return get_exercise_by_display_name(v)
                except ValueError as e:
                    raise ValueError(f"Invalid Exercise name: {v}") from e

        if isinstance(v, list):
            # Handle list representation from database
            try:
                reconstructed_value = (
                    v[0],
                    MuscleGroup(v[1]),  # Convert muscle group string back to enum
                    v[2],
                    v[3],
                    v[4],
                    v[5],
                    v[6],
                )
                return Exercise(reconstructed_value)  # Re-create enum from value
            except (IndexError, ValueError) as e:
                raise ValueError(f"Invalid exercise data from DB: {v}") from e
        return v


class WorkoutPlanScheduleBase(BaseModel):
    workoutplanScheduleId: UUID = Field(default_factory=uuid4)
    Monday: Optional[List[WorkoutPlanScheduleDay]] = Field(default_factory=list)
    Tuesday: Optional[List[WorkoutPlanScheduleDay]] = Field(default_factory=list)
    Wednesday: Optional[List[WorkoutPlanScheduleDay]] = Field(default_factory=list)
    Thursday: Optional[List[WorkoutPlanScheduleDay]] = Field(default_factory=list)
    Friday: Optional[List[WorkoutPlanScheduleDay]] = Field(default_factory=list)
    Saturday: Optional[List[WorkoutPlanScheduleDay]] = Field(default_factory=list)
    Sunday: Optional[List[WorkoutPlanScheduleDay]] = Field(default_factory=list)


class WorkoutPlanSummary(BaseModel):
    goal: str
    workout_type: str
    training_level: str
    program_duration: str
    days_per_week: int
    time_per_workout: str
    equipments: List[str]
    target_gender: str
    recommended_supplements: List[str]


class WorkoutPlanBase(BaseModel):
    user_id: str
    name: Optional[str] = None
    workoutplan_summary: WorkoutPlanSummary
    workoutplan_schedule: Optional[WorkoutPlanScheduleBase] = None


class WorkoutPlanInDB(WorkoutPlanBase):
    workoutplan_id: UUID 
