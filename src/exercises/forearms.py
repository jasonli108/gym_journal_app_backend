from exercises.base import ExerciseDefinition
from enums import MuscleGroup, EquipmentType, MechanicsType

FOREARMS_EXERCISES = {
    "FARMERS_WALK": ExerciseDefinition(id="FARMERS_WALK", display_name="Farmer's Walk", muscle_group=MuscleGroup.FOREARMS, url="https://www.muscleandstrength.com/exercises/farmers-walk.html"),
    "WRIST_CURL": ExerciseDefinition(id="WRIST_CURL", display_name="Wrist Curl", muscle_group=MuscleGroup.FOREARMS, url="https://www.muscleandstrength.com/exercises/seated-dumbbell-palms-up-wrist-curl.html"),
    "REVERSE_WRIST_CURL": ExerciseDefinition(id="REVERSE_WRIST_CURL", display_name="Reverse Wrist Curl", muscle_group=MuscleGroup.FOREARMS, url="https://www.muscleandstrength.com/exercises/seated-dumbbell-palms-down-wrist-curl.html"),
}