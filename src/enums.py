from enum import Enum


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

