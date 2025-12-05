from exercises.base import ExerciseDefinition
from enums import MuscleGroup, EquipmentType, MechanicsType

BACK_EXERCISES = {
    "PULL_UPS": ExerciseDefinition(id="PULL_UPS", display_name="Pull-ups", muscle_group=MuscleGroup.UPPER_BACK),
    "DEADLIFT": ExerciseDefinition(id="DEADLIFT", display_name="Deadlift", muscle_group=MuscleGroup.LOWER_BACK, url="https://www.muscleandstrength.com/exercises/deadlift.html", is_popular=True),
    "BENT_OVER_ROW": ExerciseDefinition(id="BENT_OVER_ROW", display_name="Bent Over Row", muscle_group=MuscleGroup.UPPER_BACK, url="https://www.muscleandstrength.com/exercises/bent-over-barbell-row.html", is_popular=True),
    "LAT_PULLDOWN": ExerciseDefinition(id="LAT_PULLDOWN", display_name="Lat Pulldown", muscle_group=MuscleGroup.LATS),
    "T_BAR_ROW": ExerciseDefinition(id="T_BAR_ROW", display_name="T-Bar Row", muscle_group=MuscleGroup.UPPER_BACK, url="https://www.muscleandstrength.com/exercises/t-bar-row.html"),
    "SEATED_CABLE_ROW": ExerciseDefinition(id="SEATED_CABLE_ROW", display_name="Seated Cable Row", muscle_group=MuscleGroup.UPPER_BACK),
    "SINGLE_ARM_DUMBBELL_ROW": ExerciseDefinition(id="SINGLE_ARM_DUMBBELL_ROW", display_name="Single Arm Dumbbell Row", muscle_group=MuscleGroup.UPPER_BACK),
    "HYPEREXTENSIONS": ExerciseDefinition(id="HYPEREXTENSIONS", display_name="Hyperextensions", muscle_group=MuscleGroup.LOWER_BACK, url="https://www.muscleandstrength.com/exercises/hyperextensions.html"),
    "BENT_OVER_DUMBBELL_ROW": ExerciseDefinition(id="BENT_OVER_DUMBBELL_ROW", display_name="Bent Over Dumbbell Row", muscle_group=MuscleGroup.UPPER_BACK, url="https://www.muscleandstrength.com/exercises/bent-over-dumbbell-row.html"),
    "PULLOWVER": ExerciseDefinition(id="PULLOWVER", display_name="Pullovers", muscle_group=MuscleGroup.LATS, url="https://www.muscleandstrength.com/exercises/straight-arm-dumbbell-pullover.html", is_popular=True),
    "SHRUGS": ExerciseDefinition(id="SHRUGS", display_name="Shrugs", muscle_group=MuscleGroup.TRAPS),
}
