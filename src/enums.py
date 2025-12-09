from enum import Enum
from typing import List, Optional


class MuscleGroup(Enum):
    ABDUCTORS = "Abductors"
    ABS = "Abs"
    ADDUCTORS = "Adductors"
    BICEPS = "Biceps"
    CALVES = "Calves"
    CHEST = "Chest"
    FOREARMS = "Forearms"
    GLUTES = "Glutes"
    HAMSTRINGS = "Hamstrings"
    HIP_FLEXORS = "Hip Flexors"
    IT_BAND = "IT Band"
    LATS = "Lats"
    LOWER_BACK = "Lower Back"
    UPPER_BACK = "Upper Back"
    NECK = "Neck"
    OBLIQUES = "Obliques"
    PALMAR_FASCIA = "Palmar Fascia"
    PLANTAR_FASCIA = "Plantar Fascia"
    QUADS = "Quads"
    SHOULDERS = "Shoulders"
    TRAPS = "Traps"
    TRICEPS = "Triceps"


class MajorMuscleGroup(Enum):
    ARMS = "Arms"
    BACK = "Back"
    CHEST = "Chest"
    LEGS = "Legs"
    ABS = "Abs"
    SHOULDER = "Shoulder"


class EquipmentType(Enum):
    BARBELL = "Barbell"
    DUMBBELL = "Dumbbell"
    MACHINE = "Machine"
    CABLE = "Cable"
    BODYWEIGHT = "Bodyweight"
    KETTLEBELL = "Kettlebell"
    BAND = "Band"
    MEDICINE_BALL = "Medicine Ball"
    EZ_BAR = "EZ Bar"
    LANDMINE = "Landmine"
    OTHER = "Other"


class MechanicsType(Enum):
    COMPOUND = "Compound"
    ISOLATION = "Isolation"


class MyCustomGroup(Enum):
    FAVORITE = "favorite"
    UNFAVORITE = "unfavorite"


class WeightUnit(str, Enum):
    KG = "kg"
    LBS = "lbs"


MAJOR_MUSCLE_GROUP_MAPPING = {
    MajorMuscleGroup.ARMS: [MuscleGroup.BICEPS, MuscleGroup.TRICEPS, MuscleGroup.FOREARMS],
    MajorMuscleGroup.BACK: [MuscleGroup.LATS, MuscleGroup.LOWER_BACK, MuscleGroup.UPPER_BACK, MuscleGroup.TRAPS],
    MajorMuscleGroup.CHEST: [MuscleGroup.CHEST],
    MajorMuscleGroup.LEGS: [MuscleGroup.ABDUCTORS, MuscleGroup.ADDUCTORS, MuscleGroup.CALVES, MuscleGroup.GLUTES, MuscleGroup.HAMSTRINGS, MuscleGroup.QUADS],
    MajorMuscleGroup.ABS: [MuscleGroup.ABS, MuscleGroup.OBLIQUES],
    MajorMuscleGroup.SHOULDER: [MuscleGroup.SHOULDERS],
}

def get_muscle_groups_for_major_group(major_muscle_group: MajorMuscleGroup) -> List[MuscleGroup]:
    return MAJOR_MUSCLE_GROUP_MAPPING.get(major_muscle_group, [])

def get_major_muscle_group(muscle_group: MuscleGroup) -> Optional[MajorMuscleGroup]:
    for major, minors in MAJOR_MUSCLE_GROUP_MAPPING.items():
        if muscle_group in minors:
            return major
    return None

