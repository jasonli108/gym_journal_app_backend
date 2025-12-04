from backend.src.exercises.base import ExerciseDefinition
from backend.src.enums import MuscleGroup, EquipmentType, MechanicsType

LEGS_EXERCISES = {
    "SQUAT": ExerciseDefinition(id="SQUAT", display_name="Squat", muscle_group=MuscleGroup.QUADS, url="https://www.muscleandstrength.com/exercises/barbell-full-squat.html"),
    "LEG_PRESS": ExerciseDefinition(id="LEG_PRESS", display_name="Leg Press", muscle_group=MuscleGroup.QUADS, url="https://www.muscleandstrength.com/exercises/leg-press.html"),
    "LUNGES": ExerciseDefinition(id="LUNGES", display_name="Lunges", muscle_group=MuscleGroup.GLUTES),
    "ROMANIAN_DEADLIFT": ExerciseDefinition(id="ROMANIAN_DEADLIFT", display_name="Romanian Deadlift", muscle_group=MuscleGroup.HAMSTRINGS, url="https://www.muscleandstrength.com/exercises/romanian-deadlift.html", is_popular=True),
    "LEG_CURLS": ExerciseDefinition(id="LEG_CURLS", display_name="Leg Curls", muscle_group=MuscleGroup.HAMSTRINGS),
    "HIP_THRUST": ExerciseDefinition(id="HIP_THRUST", display_name="Hip Thrust", muscle_group=MuscleGroup.GLUTES),
    "GOBLET_SQUAT": ExerciseDefinition(id="GOBLET_SQUAT", display_name="Goblet Squat", muscle_group=MuscleGroup.QUADS, url="https://www.muscleandstrength.com/exercises/goblet-squat.html"),
    "GOOD_MORNINGS": ExerciseDefinition(id="GOOD_MORNINGS", display_name="Good Mornings", muscle_group=MuscleGroup.HAMSTRINGS, url="https://www.muscleandstrength.com/exercises/good-morning.html"),
    "CALF_RAISES": ExerciseDefinition(id="CALF_RAISES", display_name="Calf Raises", muscle_group=MuscleGroup.CALVES),
    "LEG_EXTENSIONS": ExerciseDefinition(id="LEG_EXTENSIONS", display_name="Leg Extensions", muscle_group=MuscleGroup.QUADS, url="https://www.muscleandstrength.com/exercises/leg-extensions.html"),
    "BARBELL_HACK_SQUAT": ExerciseDefinition(id="BARBELL_HACK_SQUAT", display_name="Barbell Hack Squat", muscle_group=MuscleGroup.QUADS, url="https://www.muscleandstrength.com/exercises/barbell-hack-squat.html"),
    "BULGARIAN_SPLIT_SQUAT": ExerciseDefinition(id="BULGARIAN_SPLIT_SQUAT", display_name="Bulgarian Split Squat", muscle_group=MuscleGroup.QUADS, url="https://www.muscleandstrength.com/exercises/bulgarian-split-squat.html"),
    "FRONT_SQUAT": ExerciseDefinition(id="FRONT_SQUAT", display_name="Front Squat", muscle_group=MuscleGroup.QUADS, url="https://www.muscleandstrength.com/exercises/front-barbell-squat.html"),
    "SEATED_CALF_RAISE": ExerciseDefinition(id="SEATED_CALF_RAISE", display_name="Seated Calf Raise", muscle_group=MuscleGroup.CALVES, url="https://www.muscleandstrength.com/exercises/seated-calf-raise.html"),
    "STANDING_CALF_RAISE": ExerciseDefinition(id="STANDING_CALF_RAISE", display_name="Standing Calf Raise", muscle_group=MuscleGroup.CALVES, url="https://www.muscleandstrength.com/exercises/standing-calf-raises.html"),
    "GLUTE_HAM_RAISE": ExerciseDefinition(id="GLUTE_HAM_RAISE", display_name="Glute Ham Raise", muscle_group=MuscleGroup.HAMSTRINGS, url="https://www.muscleandstrength.com/exercises/glute-ham-raise.html"),
}
