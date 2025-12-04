from backend.src.exercises.base import ExerciseDefinition
from backend.src.enums import MuscleGroup, EquipmentType, MechanicsType

ABS_EXERCISES = {
    "CRUNCHES": ExerciseDefinition(id="CRUNCHES", display_name="Crunches", muscle_group=MuscleGroup.ABS, url="https://www.muscleandandstrength.com/exercises/crunches.html"),
    "LEG_RAISES": ExerciseDefinition(id="LEG_RAISES", display_name="Leg Raises", muscle_group=MuscleGroup.ABS),
    "PLANKS": ExerciseDefinition(id="PLANKS", display_name="Planks", muscle_group=MuscleGroup.ABS, url="https://www.muscleandstrength.com/exercises/plank.html"),
    "RUSSIAN_TWISTS": ExerciseDefinition(id="RUSSIAN_TWISTS", display_name="Russian Twists", muscle_group=MuscleGroup.OBLIQUES),
    "HANGING_KNEE_RAISES": ExerciseDefinition(id="HANGING_KNEE_RAISES", display_name="Hanging Knee Raises", muscle_group=MuscleGroup.ABS),
    "AB_WHEEL_ROLLOUT": ExerciseDefinition(id="AB_WHEEL_ROLLOUT", display_name="Ab Wheel Rollout", muscle_group=MuscleGroup.ABS, url="https://www.muscleandstrength.com/exercises/ab-roller.html"),
    "DECLINE_CRUNCH": ExerciseDefinition(id="DECLINE_CRUNCH", display_name="Decline Crunch", muscle_group=MuscleGroup.ABS, url="https://www.muscleandstrength.com/exercises/decline-crunch.html"),
    "DRAGON_FLAG": ExerciseDefinition(id="DRAGON_FLAG", display_name="Dragon Flag", muscle_group=MuscleGroup.ABS, url="https://www.muscleandstrength.com/exercises/dragon-flag.html"),
    "JACKKNIFE_SIT_UP": ExerciseDefinition(id="JACKKNIFE_SIT_UP", display_name="Jackknife Sit-up", muscle_group=MuscleGroup.ABS, url="https://www.muscleandstrength.com/exercises/jackknife-sit-up.html"),
}