from enum import Enum
from backend.src.exercises.all_exercises import ALL_EXERCISE_DEFINITIONS

Exercise = Enum(
    "Exercise",
    {ex_def.id: ex_def for ex_def in ALL_EXERCISE_DEFINITIONS.values()},
)
