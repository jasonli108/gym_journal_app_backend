from exercises.base import ExerciseDefinition
from enums import MuscleGroup, EquipmentType, MechanicsType, MajorMuscleGroup

BICEPS_EXERCISES = {
    "BARBELL_CURL": ExerciseDefinition(id="BARBELL_CURL", display_name="Barbell Curl", muscle_group=MuscleGroup.BICEPS, major_muscle_group=MajorMuscleGroup.ARMS, url="https://www.muscleandstrength.com/exercises/barbell-curl.html"),
    "DUMBBELL_CURL": ExerciseDefinition(id="DUMBBELL_CURL", display_name="Dumbbell Curl", muscle_group=MuscleGroup.BICEPS, major_muscle_group=MajorMuscleGroup.ARMS, url="https://www.muscleandstrength.com/exercises/dumbbell-curl.html"),
    "HAMMER_CURL": ExerciseDefinition(id="HAMMER_CURL", display_name="Hammer Curl", muscle_group=MuscleGroup.BICEPS, major_muscle_group=MajorMuscleGroup.ARMS, url="https://www.muscleandstrength.com/exercises/hammer-curl.html"),
    "PREACHER_CURL": ExerciseDefinition(id="PREACHER_CURL", display_name="Preacher Curl", muscle_group=MuscleGroup.BICEPS, major_muscle_group=MajorMuscleGroup.ARMS, url="https://www.muscleandstrength.com/exercises/preacher-curl.html"),
    "CONCENTRATION_CURL": ExerciseDefinition(id="CONCENTRATION_CURL", display_name="Concentration Curl", muscle_group=MuscleGroup.BICEPS, major_muscle_group=MajorMuscleGroup.ARMS, url="https://www.muscleandstrength.com/exercises/concentration-curl.html"),
    "CHIN_UPS": ExerciseDefinition(id="CHIN_UPS", display_name="Chin-ups", muscle_group=MuscleGroup.BICEPS, major_muscle_group=MajorMuscleGroup.ARMS),
    "INCLINE_DUMBBELL_CURL": ExerciseDefinition(id="INCLINE_DUMBBELL_CURL", display_name="Incline Dumbbell Curl", muscle_group=MuscleGroup.BICEPS, major_muscle_group=MajorMuscleGroup.ARMS, url="https://www.muscleandstrength.com/exercises/incline-dumbbell-curl.html"),
}
