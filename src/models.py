from datetime import date
from typing import List, Optional
from pydantic import BaseModel, Field, model_validator, validator
from uuid import UUID, uuid4
from enums import Exercise, MuscleGroup, EquipmentType, MechanicsType, MyCustomGroup

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
    sets: int
    reps: str
    weight_kg: Optional[float] = None

    @validator("exercise", pre=True)
    def convert_exercise_name_to_enum(cls, v):
        if isinstance(v, str):
            try:
                return Exercise.from_display_name(v)
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
    sets: int
    reps: str
    weight_kg: Optional[float] = None


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


from pydantic import BaseModel, Field, model_validator, validator


class WorkPlanScheduleDay(BaseModel):
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
                    return Exercise.from_display_name(v)
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


class WorkPlanScheduleBase(BaseModel):
    id: str
    monday: Optional[List[WorkPlanScheduleDay]] = None
    tuesday: Optional[List[WorkPlanScheduleDay]] = None
    wednesday: Optional[List[WorkPlanScheduleDay]] = None
    thursday: Optional[List[WorkPlanScheduleDay]] = None
    friday: Optional[List[WorkPlanScheduleDay]] = None
    saturday: Optional[List[WorkPlanScheduleDay]] = None
    sunday: Optional[List[WorkPlanScheduleDay]] = None


class WorkPlanSummary(BaseModel):
    goal: str
    workout_type: str
    training_level: str
    program_duration: str
    days_per_week: int
    time_per_workout: str
    equipments: List[str]
    target_gender: str
    recommended_supplements: List[str]


class WorkPlanBase(BaseModel):
    user_id: str
    workplan_summary: WorkPlanSummary
    workplan_schedule: Optional[WorkPlanScheduleBase] = None


class WorkPlanInDB(WorkPlanBase):
    workplan_id: UUID 
