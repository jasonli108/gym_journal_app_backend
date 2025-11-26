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


class Exercise(Enum):
    # Existing exercises re-mapped to new MuscleGroup structure
    # Chest
    BENCH_PRESS = ("Bench Press", MuscleGroup.CHEST, None, False, None, None, None)
    DUMBBELL_PRESS = ("Dumbbell Press", MuscleGroup.CHEST, None, False, None, None, None)
    INCLINE_BENCH_PRESS = ("Incline Bench Press", MuscleGroup.CHEST, None, False, None, None, None)
    PUSH_UPS = ("Push-ups", MuscleGroup.CHEST, None, False, None, None, None)
    DUMBBELL_FLYES = ("Dumbbell Flyes", MuscleGroup.CHEST, None, False, None, None, None)
    CABLE_CROSSOVER = ("Cable Crossover", MuscleGroup.CHEST, None, False, None, None, None)
    CHEST_DIPS = ("Chest Dips", MuscleGroup.CHEST, None, False, None, None, None)
    PEC_DECK = ("Pec Deck Machine", MuscleGroup.CHEST, None, False, None, None, None)

    # Back (now Upper Back, Lower Back, Lats)
    PULL_UPS = ("Pull-ups", MuscleGroup.UPPER_BACK, None, False, None, None, None)
    DEADLIFT = ("Deadlift", MuscleGroup.LOWER_BACK, "https://www.muscleandstrength.com/exercises/deadlift.html", True, None, None, None)
    BENT_OVER_ROW = ("Bent Over Row", MuscleGroup.UPPER_BACK, "https://www.muscleandstrength.com/exercises/bent-over-barbell-row.html", True, None, None, None)
    LAT_PULLDOWN = ("Lat Pulldown", MuscleGroup.LATS, None, False, None, None, None)
    T_BAR_ROW = ("T-Bar Row", MuscleGroup.UPPER_BACK, "https://www.muscleandstrength.com/exercises/t-bar-row.html", False, None, None, None)
    SEATED_CABLE_ROW = ("Seated Cable Row", MuscleGroup.UPPER_BACK, None, False, None, None, None)
    SINGLE_ARM_DUMBBELL_ROW = ("Single Arm Dumbbell Row", MuscleGroup.UPPER_BACK, None, False, None, None, None)
    HYPEREXTENSIONS = ("Hyperextensions", MuscleGroup.LOWER_BACK, "https://www.muscleandstrength.com/exercises/hyperextensions.html", False, None, None, None)

    # Shoulders
    OVERHEAD_PRESS = ("Overhead Press", MuscleGroup.SHOULDERS, "https://www.muscleandstrength.com/exercises/standing-military-press.html", True, None, None, None)
    LATERAL_RAISE = ("Lateral Raise", MuscleGroup.SHOULDERS, None, False, None, None, None)
    FRONT_RAISE = ("Front Raise", MuscleGroup.SHOULDERS, None, False, None, None, None)
    FACE_PULLS = ("Face Pulls", MuscleGroup.SHOULDERS, None, False, None, None, None)
    ARNOLD_PRESS = ("Arnold Press", MuscleGroup.SHOULDERS, "https://www.muscleandstrength.com/exercises/arnold-press.html", True, None, None, None)
    SHRUGS = ("Shrugs", MuscleGroup.TRAPS, None, False, None, None, None)
    REAR_DELT_FLYE = ("Rear Delt Flye", MuscleGroup.SHOULDERS, None, False, None, None, None)

    # Biceps
    BARBELL_CURL = ("Barbell Curl", MuscleGroup.BICEPS, "https://www.muscleandstrength.com/exercises/barbell-curl.html", False, None, None, None)
    DUMBBELL_CURL = ("Dumbbell Curl", MuscleGroup.BICEPS, "https://www.muscleandstrength.com/exercises/dumbbell-curl.html", False, None, None, None)
    HAMMER_CURL = ("Hammer Curl", MuscleGroup.BICEPS, "https://www.muscleandstrength.com/exercises/hammer-curl.html", False, None, None, None)
    PREACHER_CURL = ("Preacher Curl", MuscleGroup.BICEPS, "https://www.muscleandstrength.com/exercises/preacher-curl.html", False, None, None, None)
    CONCENTRATION_CURL = ("Concentration Curl", MuscleGroup.BICEPS, "https://www.muscleandstrength.com/exercises/concentration-curl.html", False, None, None, None)
    CHIN_UPS = ("Chin-ups", MuscleGroup.BICEPS, None, False, None, None, None)

    # Triceps
    TRICEP_DIP = ("Tricep Dip", MuscleGroup.TRICEPS, "https://www.muscleandstrength.com/exercises/dips-triceps-version.html", False, None, None, None)
    SKULL_CRUSHERS = ("Skull Crushers", MuscleGroup.TRICEPS, "https://www.muscleandstrength.com/exercises/lying-triceps-press.html", False, None, None, None)
    TRICEP_PUSHDOWN = ("Tricep Pushdown", MuscleGroup.TRICEPS, None, False, None, None, None)
    OVERHEAD_TRICEP_EXTENSION = ("Overhead Tricep Extension", MuscleGroup.TRICEPS, None, False, None, None, None)
    CLOSE_GRIP_BENCH_PRESS = ("Close Grip Bench Press", MuscleGroup.TRICEPS, "https://www.muscleandstrength.com/exercises/close-grip-barbell-bench-press.html", False, None, None, None)

    # Legs
    SQUAT = ("Squat", MuscleGroup.QUADS, "https://www.muscleandstrength.com/exercises/barbell-full-squat.html", False, None, None, None)
    LEG_PRESS = ("Leg Press", MuscleGroup.QUADS, "https://www.muscleandstrength.com/exercises/leg-press.html", False, None, None, None)
    LUNGES = ("Lunges", MuscleGroup.GLUTES, None, False, None, None, None)
    ROMANIAN_DEADLIFT = ("Romanian Deadlift", MuscleGroup.HAMSTRINGS, "https://www.muscleandstrength.com/exercises/romanian-deadlift.html", True, None, None, None)
    LEG_CURLS = ("Leg Curls", MuscleGroup.HAMSTRINGS, None, False, None, None, None)
    HIP_THRUST = ("Hip Thrust", MuscleGroup.GLUTES, None, False, None, None, None)
    GOBLET_SQUAT = ("Goblet Squat", MuscleGroup.QUADS, "https://www.muscleandstrength.com/exercises/goblet-squat.html", False, None, None, None)
    GOOD_MORNINGS = ("Good Mornings", MuscleGroup.HAMSTRINGS, "https://www.muscleandstrength.com/exercises/good-morning.html", False, None, None, None)
    CALF_RAISES = ("Calf Raises", MuscleGroup.CALVES, None, False, None, None, None)
    LEG_EXTENSIONS = ("Leg Extensions", MuscleGroup.QUADS, "https://www.muscleandstrength.com/exercises/leg-extensions.html", False, None, None, None)
    
    # Abs & Core
    CRUNCHES = ("Crunches", MuscleGroup.ABS, "https://www.muscleandstrength.com/exercises/crunches.html", False, None, None, None)
    LEG_RAISES = ("Leg Raises", MuscleGroup.ABS, None, False, None, None, None)
    PLANKS = ("Planks", MuscleGroup.ABS, "https://www.muscleandstrength.com/exercises/plank.html", False, None, None, None)
    RUSSIAN_TWISTS = ("Russian Twists", MuscleGroup.OBLIQUES, None, False, None, None, None)
    HANGING_KNEE_RAISES = ("Hanging Knee Raises", MuscleGroup.ABS, None, False, None, None, None)
    AB_WHEEL_ROLLOUT = ("Ab Wheel Rollout", MuscleGroup.ABS, "https://www.muscleandstrength.com/exercises/ab-roller.html", False, None, None, None)

    # --- NEWLY ADDED EXERCISES ---
    # Chest
    DECLINE_DUMBBELL_BENCH_PRESS = ("Decline Dumbbell Bench Press", MuscleGroup.CHEST, "https://www.muscleandstrength.com/exercises/decline-dumbbell-bench-press.html", False, None, None, None)
    INCLINE_DUMBBELL_BENCH_PRESS = ("Incline Dumbbell Bench Press", MuscleGroup.CHEST, "https://www.muscleandstrength.com/exercises/incline-dumbbell-press.html", False, None, None, None)
    
    # Back
    BENT_OVER_DUMBBELL_ROW = ("Bent Over Dumbbell Row", MuscleGroup.UPPER_BACK, "https://www.muscleandstrength.com/exercises/bent-over-dumbbell-row.html", False, None, None, None)
    PULLOWVER = ("Pullovers", MuscleGroup.LATS, "https://www.muscleandstrength.com/exercises/straight-arm-dumbbell-pullover.html", True, None, None, None)

    # Shoulders
    SEATED_DUMBBELL_PRESS = ("Seated Dumbbell Press", MuscleGroup.SHOULDERS, "https://www.muscleandstrength.com/exercises/seated-dumbbell-press.html", False, None, None, None)
    UPRIGHT_ROW = ("Upright Row", MuscleGroup.SHOULDERS, "https://www.muscleandstrength.com/exercises/upright-barbell-row.html", False, None, None, None)

    # Biceps
    INCLINE_DUMBBELL_CURL = ("Incline Dumbbell Curl", MuscleGroup.BICEPS, "https://www.muscleandstrength.com/exercises/incline-dumbbell-curl.html", False, None, None, None)
    
    # Triceps
    BENCH_DIP = ("Bench Dip", MuscleGroup.TRICEPS, "https://www.muscleandstrength.com/exercises/bench-dips.html", False, None, None, None)

    # Legs
    BARBELL_HACK_SQUAT = ("Barbell Hack Squat", MuscleGroup.QUADS, "https://www.muscleandstrength.com/exercises/barbell-hack-squat.html", False, None, None, None)
    BULGARIAN_SPLIT_SQUAT = ("Bulgarian Split Squat", MuscleGroup.QUADS, "https://www.muscleandstrength.com/exercises/bulgarian-split-squat.html", False, None, None, None)
    FRONT_SQUAT = ("Front Squat", MuscleGroup.QUADS, "https://www.muscleandstrength.com/exercises/front-barbell-squat.html", False, None, None, None)
    SEATED_CALF_RAISE = ("Seated Calf Raise", MuscleGroup.CALVES, "https://www.muscleandstrength.com/exercises/seated-calf-raise.html", False, None, None, None)
    STANDING_CALF_RAISE = ("Standing Calf Raise", MuscleGroup.CALVES, "https://www.muscleandstrength.com/exercises/standing-calf-raises.html", False, None, None, None)
    GLUTE_HAM_RAISE = ("Glute Ham Raise", MuscleGroup.HAMSTRINGS, "https://www.muscleandstrength.com/exercises/glute-ham-raise.html", False, None, None, None)

    # Abs
    DECLINE_CRUNCH = ("Decline Crunch", MuscleGroup.ABS, "https://www.muscleandstrength.com/exercises/decline-crunch.html", False, None, None, None)
    DRAGON_FLAG = ("Dragon Flag", MuscleGroup.ABS, "https://www.muscleandstrength.com/exercises/dragon-flag.html", False, None, None, None)
    JACKKNIFE_SIT_UP = ("Jackknife Sit-up", MuscleGroup.ABS, "https://www.muscleandstrength.com/exercises/jackknife-sit-up.html", False, None, None, None)
    
    # Forearms
    FARMERS_WALK = ("Farmer's Walk", MuscleGroup.FOREARMS, "https://www.muscleandstrength.com/exercises/farmers-walk.html", False, None, None, None)
    WRIST_CURL = ("Wrist Curl", MuscleGroup.FOREARMS, "https://www.muscleandstrength.com/exercises/seated-dumbbell-palms-up-wrist-curl.html", False, None, None, None)
    REVERSE_WRIST_CURL = ("Reverse Wrist Curl", MuscleGroup.FOREARMS, "https://www.muscleandstrength.com/exercises/seated-dumbbell-palms-down-wrist-curl.html", False, None, None, None)


    def __init__(self, display_name, muscle_group, url=None, is_popular=False, equipment_type=None, mechanics_type=None, my_custom_group=None):
        self.display_name = display_name
        self.muscle_group = muscle_group
        self.url = url
        self.is_popular = is_popular
        self.equipment_type = equipment_type
        self.mechanics_type = mechanics_type
        self.my_custom_group = my_custom_group

    @classmethod
    def from_display_name(cls, display_name: str):
        for member in cls:
            if member.display_name == display_name:
                return member
        raise ValueError(f"No Exercise with display name '{display_name}'")    

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
    OTHER = "Other"

class MechanicsType(Enum):
    COMPOUND = "Compound"
    ISOLATION = "Isolation"

class MyCustomGroup(Enum):
    FAVORITE="favorite"
    UNFAVORITE="unfavorite"
