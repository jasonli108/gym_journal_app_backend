from backend.src.exercises.base import ExerciseDefinition
from backend.src.enums import MuscleGroup, EquipmentType, MechanicsType

SHOULDERS_EXERCISES = {
    "OVERHEAD_PRESS": ExerciseDefinition(id="OVERHEAD_PRESS", display_name="Overhead Press", muscle_group=MuscleGroup.SHOULDERS, url="https://www.muscleandstrength.com/exercises/standing-military-press.html", is_popular=True),
    "LATERAL_RAISE": ExerciseDefinition(id="LATERAL_RAISE", display_name="Lateral Raise", muscle_group=MuscleGroup.SHOULDERS),
    "FRONT_RAISE": ExerciseDefinition(id="FRONT_RAISE", display_name="Front Raise", muscle_group=MuscleGroup.SHOULDERS),
    "FACE_PULLS": ExerciseDefinition(id="FACE_PULLS", display_name="Face Pulls", muscle_group=MuscleGroup.SHOULDERS),
    "ARNOLD_PRESS": ExerciseDefinition(id="ARNOLD_PRESS", display_name="Arnold Press", muscle_group=MuscleGroup.SHOULDERS, url="https://www.muscleandstrength.com/exercises/arnold-press.html", is_popular=True),
    "REAR_DELT_FLYE": ExerciseDefinition(id="REAR_DELT_FLYE", display_name="Rear Delt Flye", muscle_group=MuscleGroup.SHOULDERS),
    "SEATED_DUMBBELL_PRESS": ExerciseDefinition(id="SEATED_DUMBBELL_PRESS", display_name="Seated Dumbbell Press", muscle_group=MuscleGroup.SHOULDERS, url="https://www.muscleandstrength.com/exercises/seated-dumbbell-press.html"),
    "UPRIGHT_ROW": ExerciseDefinition(id="UPRIGHT_ROW", display_name="Upright Row", muscle_group=MuscleGroup.SHOULDERS, url="https://www.muscleandstrength.com/exercises/upright-barbell-row.html"),
    "CABLE_EXTERNAL_ROTATION_AT_90_DEGREES": ExerciseDefinition(
        id="CABLE_EXTERNAL_ROTATION_AT_90_DEGREES",
        display_name="Cable External Rotation at 90 Degrees",
        muscle_group=MuscleGroup.SHOULDERS,
        equipment_type=EquipmentType.CABLE,
        mechanics_type=MechanicsType.ISOLATION,
    ),
    "CABLE_INTERNAL_ROTATION_AT_90_DEGREES": ExerciseDefinition(
        id="CABLE_INTERNAL_ROTATION_AT_90_DEGREES",
        display_name="Cable Internal Rotation at 90 Degrees",
        muscle_group=MuscleGroup.SHOULDERS,
        equipment_type=EquipmentType.CABLE,
        mechanics_type=MechanicsType.ISOLATION,
    ),
}