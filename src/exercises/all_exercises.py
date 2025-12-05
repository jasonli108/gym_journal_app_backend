from typing import List, Dict
from exercises.base import ExerciseDefinition
from enums import MuscleGroup, EquipmentType, MechanicsType # Import necessary enums

# Import all muscle group exercise dictionaries
from .abs import ABS_EXERCISES
from .adductors import ADDUCTORS_EXERCISES
from .abductors import ABDUCTORS_EXERCISES
from .back import BACK_EXERCISES
from .biceps import BICEPS_EXERCISES
from .calves import CALVES_EXERCISES
from .chest import CHEST_EXERCISES
from .forearms import FOREARMS_EXERCISES
from .glutes import GLUTES_EXERCISES
from .hamstrings import HAMSTRINGS_EXERCISES
from .hip_flexors import HIP_FLEXORS_EXERCISES
from .it_band import IT_BAND_EXERCISES
from .lats import LATS_EXERCISES
from .legs import LEGS_EXERCISES
from .lower_back import LOWER_BACK_EXERCISES
from .neck import NECK_EXERCISES
from .obliques import OBLIQUES_EXERCISES
from .palmar_fascia import PALMAR_FASCIA_EXERCISES
from .plantar_fascia import PLANTAR_FASCIA_EXERCISES
from .quads import QUADS_EXERCISES
from .shoulders import SHOULDERS_EXERCISES
from .traps import TRAPS_EXERCISES
from .triceps import TRICEPS_EXERCISES
from .upper_back import UPPER_BACK_EXERCISES


ALL_EXERCISE_DEFINITIONS: Dict[str, ExerciseDefinition] = {}

def add_exercises_from_dict(exercise_dict: Dict[str, ExerciseDefinition]):
    ALL_EXERCISE_DEFINITIONS.update(exercise_dict)

add_exercises_from_dict(ABS_EXERCISES)
add_exercises_from_dict(ADDUCTORS_EXERCISES)
add_exercises_from_dict(ABDUCTORS_EXERCISES)
add_exercises_from_dict(BACK_EXERCISES)
add_exercises_from_dict(BICEPS_EXERCISES)
add_exercises_from_dict(CALVES_EXERCISES)
add_exercises_from_dict(CHEST_EXERCISES)
add_exercises_from_dict(FOREARMS_EXERCISES)
add_exercises_from_dict(GLUTES_EXERCISES)
add_exercises_from_dict(HAMSTRINGS_EXERCISES)
add_exercises_from_dict(HIP_FLEXORS_EXERCISES)
add_exercises_from_dict(IT_BAND_EXERCISES)
add_exercises_from_dict(LATS_EXERCISES)
add_exercises_from_dict(LEGS_EXERCISES)
add_exercises_from_dict(LOWER_BACK_EXERCISES)
add_exercises_from_dict(NECK_EXERCISES)
add_exercises_from_dict(OBLIQUES_EXERCISES)
add_exercises_from_dict(PALMAR_FASCIA_EXERCISES)
add_exercises_from_dict(PLANTAR_FASCIA_EXERCISES)
add_exercises_from_dict(QUADS_EXERCISES)
add_exercises_from_dict(SHOULDERS_EXERCISES)
add_exercises_from_dict(TRAPS_EXERCISES)
add_exercises_from_dict(TRICEPS_EXERCISES)
add_exercises_from_dict(UPPER_BACK_EXERCISES)



EXERCISES_BY_MUSCLE_GROUP: Dict[MuscleGroup, Dict[str, ExerciseDefinition]] = {
    group: {} for group in MuscleGroup
}
for exercise_def in ALL_EXERCISE_DEFINITIONS.values():
    EXERCISES_BY_MUSCLE_GROUP[exercise_def.muscle_group][
        exercise_def.id
    ] = exercise_def

# Create a dictionary for quick lookup by display_name
EXERCISE_BY_DISPLAY_NAME: Dict[str, ExerciseDefinition] = {
    ex.display_name: ex for ex in ALL_EXERCISE_DEFINITIONS.values()
}

def get_exercises_by_muscle_group(
    muscle_group: MuscleGroup,
) -> Dict[str, ExerciseDefinition]:
    """Returns a dictionary of exercise definitions for a given muscle group."""
    return EXERCISES_BY_MUSCLE_GROUP.get(muscle_group, {})

def get_exercise_by_display_name(display_name: str) -> ExerciseDefinition:
    """Looks up an exercise by its display name."""
    exercise = EXERCISE_BY_DISPLAY_NAME.get(display_name)
    if not exercise:
        raise ValueError(f"No Exercise with display name '{display_name}'")
    return exercise

def get_exercise_by_id(exercise_id: str) -> ExerciseDefinition:
    """Looks up an exercise by its ID."""
    exercise = ALL_EXERCISE_DEFINITIONS.get(exercise_id)
    if not exercise:
        raise ValueError(f"No Exercise with ID '{exercise_id}'")
    return exercise
