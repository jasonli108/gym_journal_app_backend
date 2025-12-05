from exercises.base import ExerciseDefinition
from enums import MuscleGroup, EquipmentType, MechanicsType

TRICEPS_EXERCISES = {
    "TRICEP_DIP": ExerciseDefinition(id="TRICEP_DIP", display_name="Tricep Dip", muscle_group=MuscleGroup.TRICEPS, url="https://www.muscleandstrength.com/exercises/dips-triceps-version.html"),
    "SKULL_CRUSHERS": ExerciseDefinition(id="SKULL_CRUSHERS", display_name="Skull Crushers", muscle_group=MuscleGroup.TRICEPS, url="https://www.muscleandstrength.com/exercises/lying-triceps-press.html"),
    "TRICEP_PUSHDOWN": ExerciseDefinition(id="TRICEP_PUSHDOWN", display_name="Tricep Pushdown", muscle_group=MuscleGroup.TRICEPS),
    "OVERHEAD_TRICEP_EXTENSION": ExerciseDefinition(id="OVERHEAD_TRICEP_EXTENSION", display_name="Overhead Tricep Extension", muscle_group=MuscleGroup.TRICEPS),
    "CLOSE_GRIP_BENCH_PRESS": ExerciseDefinition(id="CLOSE_GRIP_BENCH_PRESS", display_name="Close Grip Bench Press", muscle_group=MuscleGroup.TRICEPS, url="https://www.muscleandstrength.com/exercises/close-grip-barbell-bench-press.html"),
    "BENCH_DIP": ExerciseDefinition(id="BENCH_DIP", display_name="Bench Dip", muscle_group=MuscleGroup.TRICEPS, url="https://www.muscleandstrength.com/exercises/bench-dips.html"),
}