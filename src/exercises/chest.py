from backend.src.exercises.base import ExerciseDefinition
from backend.src.enums import MuscleGroup, EquipmentType, MechanicsType

CHEST_EXERCISES = {
    "BENCH_PRESS": ExerciseDefinition(id="BENCH_PRESS", display_name="Bench Press", muscle_group=MuscleGroup.CHEST),
    "DUMBBELL_PRESS": ExerciseDefinition(id="DUMBBELL_PRESS", display_name="Dumbbell Press", muscle_group=MuscleGroup.CHEST),
    "INCLINE_BENCH_PRESS": ExerciseDefinition(id="INCLINE_BENCH_PRESS", display_name="Incline Bench Press", muscle_group=MuscleGroup.CHEST),
    "PUSH_UPS": ExerciseDefinition(id="PUSH_UPS", display_name="Push-ups", muscle_group=MuscleGroup.CHEST),
    "DUMBBELL_FLYES": ExerciseDefinition(id="DUMBBELL_FLYES", display_name="Dumbbell Flyes", muscle_group=MuscleGroup.CHEST),
    "CABLE_CROSSOVER": ExerciseDefinition(id="CABLE_CROSSOVER", display_name="Cable Crossover", muscle_group=MuscleGroup.CHEST),
    "CHEST_DIPS": ExerciseDefinition(id="CHEST_DIPS", display_name="Chest Dips", muscle_group=MuscleGroup.CHEST),
    "PEC_DECK": ExerciseDefinition(id="PEC_DECK", display_name="Pec Deck Machine", muscle_group=MuscleGroup.CHEST),
    "DECLINE_DUMBBELL_BENCH_PRESS": ExerciseDefinition(id="DECLINE_DUMBBELL_BENCH_PRESS", display_name="Decline Dumbbell Bench Press", muscle_group=MuscleGroup.CHEST, url="https://www.muscleandstrength.com/exercises/decline-dumbbell-bench-press.html"),
    "INCLINE_DUMBBELL_BENCH_PRESS": ExerciseDefinition(id="INCLINE_DUMBBELL_BENCH_PRESS", display_name="Incline Dumbbell Bench Press", muscle_group=MuscleGroup.CHEST, url="https://www.muscleandstrength.com/exercises/incline-dumbbell-press.html"),
    "INCLINE_DUMBBELL_PRESS": ExerciseDefinition(id="INCLINE_DUMBBELL_PRESS", display_name="Incline Dumbbell Press", muscle_group=MuscleGroup.CHEST, url="https://www.muscleandstrength.com/exercises/incline-dumbbell-press.html", is_popular=True, equipment_type=EquipmentType.DUMBBELL, mechanics_type=MechanicsType.COMPOUND),
    "DECLINE_DUMBBELL_PRESS": ExerciseDefinition(id="DECLINE_DUMBBELL_PRESS", display_name="Decline Dumbbell Press", muscle_group=MuscleGroup.CHEST, url="https://www.muscleandstrength.com/exercises/decline-dumbbell-press.html", equipment_type=EquipmentType.DUMBBELL, mechanics_type=MechanicsType.COMPOUND),
    "DUMBBELL_PULLOVER": ExerciseDefinition(id="DUMBBELL_PULLOVER", display_name="Dumbbell Pullover", muscle_group=MuscleGroup.CHEST, url="https://www.muscleandstrength.com/exercises/dumbbell-pullover.html", equipment_type=EquipmentType.DUMBBELL, mechanics_type=MechanicsType.ISOLATION),
    "SVEND_PRESS": ExerciseDefinition(id="SVEND_PRESS", display_name="Svend Press", muscle_group=MuscleGroup.CHEST, url="https://www.muscleandstrength.com/exercises/svend-press.html", equipment_type=EquipmentType.OTHER, mechanics_type=MechanicsType.ISOLATION),
    "CLOSE_GRIP_DUMBBELL_PRESS": ExerciseDefinition(id="CLOSE_GRIP_DUMBBELL_PRESS", display_name="Close Grip Dumbbell Press", muscle_group=MuscleGroup.CHEST, url="https://www.muscleandstrength.com/exercises/close-grip-dumbbell-press.html", equipment_type=EquipmentType.DUMBBELL, mechanics_type=MechanicsType.COMPOUND),
    "INCLINE_DUMBBELL_FLY": ExerciseDefinition(id="INCLINE_DUMBBELL_FLY", display_name="Incline Dumbbell Fly", muscle_group=MuscleGroup.CHEST, url="https://www.muscleandstrength.com/exercises/incline-dumbbell-fly.html", equipment_type=EquipmentType.DUMBBELL, mechanics_type=MechanicsType.ISOLATION),
}