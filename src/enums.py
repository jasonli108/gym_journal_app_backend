from enum import Enum
from typing import List, Optional


class MuscleGroup(Enum):
    ABDUCTORS = "Abductors"
    ABS = "Abs"
    ADDUCTORS = "Adductors"
    AUTO_BELAY_TOP_ROPING = "Auto Belay Top Roping"
    BICEPS = "Biceps"
    BOULDERING = "Bouldering"
    CALVES = "Calves"
    CHEST = "Chest"
    FOREARMS = "Forearms"
    GLUTES = "Glutes"
    HAMSTRINGS = "Hamstrings"
    HIP_FLEXORS = "Hip Flexors"
    LATS = "Lats"
    LEAD_CLIMBING = "Lead Climbing"
    LOWER_BACK = "Lower Back"
    NECK = "Neck"
    QUADS = "Quads"
    SHOULDERS = "Shoulders"
    TOP_ROPING = "Top Roping"
    TRAPS = "Traps"
    TRICEPS = "Triceps"


class MajorMuscleGroup(Enum):
    ABS = "Abs"
    ARMS = "Arms"
    BACK = "Back"
    CHEST = "Chest"
    CLIMBING = "Climbing"
    LEGS = "Legs"
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
    CLIMBING_WALL = "Climbing Wall"


class MechanicsType(Enum):
    COMPOUND = "Compound"
    ISOLATION = "Isolation"


class ForceType(Enum):
    STATIC = "Static"
    PULL = "Pull"
    PUSH = "Push"


class LevelType(Enum):
    BEGINNER = "Beginner"
    INTERMEDIATE = "Intermediate"
    EXPERT = "Expert"
    ADVANCED = "Advanced"
    PRO = "Professional"
    JEDI = "Jedi"
    CLIMBING_DEMI_GOD = "Climbing Demi-God"


class CategoryType(Enum):
    POWERLIFTING = "Powerlifting"
    STRENGTH = "Strength"
    STRETCHING = "Stretching"
    CARDIO = "Cardio"
    OLYMPIC_WEIGHTLIFTING = "Olympic Weightlifting"
    STRONGMAN = "Strongman"
    PLYOMETRICS = "Plyometrics"


class MyCustomGroup(Enum):
    FAVORITE = "favorite"
    UNFAVORITE = "unfavorite"


class WeightUnit(str, Enum):
    KG = "kg"
    LBS = "lbs"


MAJOR_MUSCLE_GROUP_MAPPING = {
    MajorMuscleGroup.ARMS: [MuscleGroup.BICEPS, MuscleGroup.TRICEPS, MuscleGroup.FOREARMS],
    MajorMuscleGroup.BACK: [MuscleGroup.LATS, MuscleGroup.LOWER_BACK, MuscleGroup.TRAPS],
    MajorMuscleGroup.CHEST: [MuscleGroup.CHEST],
    MajorMuscleGroup.LEGS: [MuscleGroup.ABDUCTORS, MuscleGroup.ADDUCTORS, MuscleGroup.CALVES, MuscleGroup.GLUTES, MuscleGroup.HAMSTRINGS, MuscleGroup.QUADS],
    MajorMuscleGroup.ABS: [MuscleGroup.ABS],
    MajorMuscleGroup.SHOULDER: [MuscleGroup.SHOULDERS],
    MajorMuscleGroup.CLIMBING: [MuscleGroup.AUTO_BELAY_TOP_ROPING, MuscleGroup.BOULDERING, MuscleGroup.LEAD_CLIMBING, MuscleGroup.TOP_ROPING],
}

def get_muscle_groups_for_major_group(major_muscle_group: MajorMuscleGroup) -> List[MuscleGroup]:
    return MAJOR_MUSCLE_GROUP_MAPPING.get(major_muscle_group, [])

def get_major_muscle_group(muscle_group: MuscleGroup) -> Optional[MajorMuscleGroup]:
    for major, minors in MAJOR_MUSCLE_GROUP_MAPPING.items():
        if muscle_group in minors:
            return major
    return None

