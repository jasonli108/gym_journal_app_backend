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


class Exercise(Enum):
    # Existing exercises re-mapped to new MuscleGroup structure
    # Chest
    BENCH_PRESS = ("Bench Press", MuscleGroup.CHEST, None, False, None, None, None)
    DUMBBELL_PRESS = (
        "Dumbbell Press",
        MuscleGroup.CHEST,
        None,
        False,
        None,
        None,
        None,
    )
    INCLINE_BENCH_PRESS = (
        "Incline Bench Press",
        MuscleGroup.CHEST,
        None,
        False,
        None,
        None,
        None,
    )
    PUSH_UPS = ("Push-ups", MuscleGroup.CHEST, None, False, None, None, None)
    DUMBBELL_FLYES = (
        "Dumbbell Flyes",
        MuscleGroup.CHEST,
        None,
        False,
        None,
        None,
        None,
    )
    CABLE_CROSSOVER = (
        "Cable Crossover",
        MuscleGroup.CHEST,
        None,
        False,
        None,
        None,
        None,
    )
    CHEST_DIPS = ("Chest Dips", MuscleGroup.CHEST, None, False, None, None, None)
    PEC_DECK = ("Pec Deck Machine", MuscleGroup.CHEST, None, False, None, None, None)

    # Back (now Upper Back, Lower Back, Lats)
    PULL_UPS = ("Pull-ups", MuscleGroup.UPPER_BACK, None, False, None, None, None)
    DEADLIFT = (
        "Deadlift",
        MuscleGroup.LOWER_BACK,
        "https://www.muscleandstrength.com/exercises/deadlift.html",
        True,
        None,
        None,
        None,
    )
    BENT_OVER_ROW = (
        "Bent Over Row",
        MuscleGroup.UPPER_BACK,
        "https://www.muscleandstrength.com/exercises/bent-over-barbell-row.html",
        True,
        None,
        None,
        None,
    )
    LAT_PULLDOWN = ("Lat Pulldown", MuscleGroup.LATS, None, False, None, None, None)
    T_BAR_ROW = (
        "T-Bar Row",
        MuscleGroup.UPPER_BACK,
        "https://www.muscleandstrength.com/exercises/t-bar-row.html",
        False,
        None,
        None,
        None,
    )
    SEATED_CABLE_ROW = (
        "Seated Cable Row",
        MuscleGroup.UPPER_BACK,
        None,
        False,
        None,
        None,
        None,
    )
    SINGLE_ARM_DUMBBELL_ROW = (
        "Single Arm Dumbbell Row",
        MuscleGroup.UPPER_BACK,
        None,
        False,
        None,
        None,
        None,
    )
    HYPEREXTENSIONS = (
        "Hyperextensions",
        MuscleGroup.LOWER_BACK,
        "https://www.muscleandstrength.com/exercises/hyperextensions.html",
        False,
        None,
        None,
        None,
    )

    # Shoulders
    OVERHEAD_PRESS = (
        "Overhead Press",
        MuscleGroup.SHOULDERS,
        "https://www.muscleandstrength.com/exercises/standing-military-press.html",
        True,
        None,
        None,
        None,
    )
    LATERAL_RAISE = (
        "Lateral Raise",
        MuscleGroup.SHOULDERS,
        None,
        False,
        None,
        None,
        None,
    )
    FRONT_RAISE = ("Front Raise", MuscleGroup.SHOULDERS, None, False, None, None, None)
    FACE_PULLS = ("Face Pulls", MuscleGroup.SHOULDERS, None, False, None, None, None)
    ARNOLD_PRESS = (
        "Arnold Press",
        MuscleGroup.SHOULDERS,
        "https://www.muscleandstrength.com/exercises/arnold-press.html",
        True,
        None,
        None,
        None,
    )
    SHRUGS = ("Shrugs", MuscleGroup.TRAPS, None, False, None, None, None)
    REAR_DELT_FLYE = (
        "Rear Delt Flye",
        MuscleGroup.SHOULDERS,
        None,
        False,
        None,
        None,
        None,
    )
    CABLE_EXTERNAL_ROTATION_AT_90_DEGREES = (
        "Cable External Rotation at 90 Degrees",
        MuscleGroup.SHOULDERS,
        None,
        False,
        EquipmentType.CABLE,
        MechanicsType.ISOLATION,
        None,
    )
    CABLE_INTERNAL_ROTATION_AT_90_DEGREES = (
        "Cable Internal Rotation at 90 Degrees",
        MuscleGroup.SHOULDERS,
        None,
        False,
        EquipmentType.CABLE,
        MechanicsType.ISOLATION,
        None,
    )

    # Biceps
    BARBELL_CURL = (
        "Barbell Curl",
        MuscleGroup.BICEPS,
        "https://www.muscleandstrength.com/exercises/barbell-curl.html",
        False,
        None,
        None,
        None,
    )
    DUMBBELL_CURL = (
        "Dumbbell Curl",
        MuscleGroup.BICEPS,
        "https://www.muscleandstrength.com/exercises/dumbbell-curl.html",
        False,
        None,
        None,
        None,
    )
    HAMMER_CURL = (
        "Hammer Curl",
        MuscleGroup.BICEPS,
        "https://www.muscleandstrength.com/exercises/hammer-curl.html",
        False,
        None,
        None,
        None,
    )
    PREACHER_CURL = (
        "Preacher Curl",
        MuscleGroup.BICEPS,
        "https://www.muscleandstrength.com/exercises/preacher-curl.html",
        False,
        None,
        None,
        None,
    )
    CONCENTRATION_CURL = (
        "Concentration Curl",
        MuscleGroup.BICEPS,
        "https://www.muscleandstrength.com/exercises/concentration-curl.html",
        False,
        None,
        None,
        None,
    )
    CHIN_UPS = ("Chin-ups", MuscleGroup.BICEPS, None, False, None, None, None)

    # Triceps
    TRICEP_DIP = (
        "Tricep Dip",
        MuscleGroup.TRICEPS,
        "https://www.muscleandstrength.com/exercises/dips-triceps-version.html",
        False,
        None,
        None,
        None,
    )
    SKULL_CRUSHERS = (
        "Skull Crushers",
        MuscleGroup.TRICEPS,
        "https://www.muscleandstrength.com/exercises/lying-triceps-press.html",
        False,
        None,
        None,
        None,
    )
    TRICEP_PUSHDOWN = (
        "Tricep Pushdown",
        MuscleGroup.TRICEPS,
        None,
        False,
        None,
        None,
        None,
    )
    OVERHEAD_TRICEP_EXTENSION = (
        "Overhead Tricep Extension",
        MuscleGroup.TRICEPS,
        None,
        False,
        None,
        None,
        None,
    )
    CLOSE_GRIP_BENCH_PRESS = (
        "Close Grip Bench Press",
        MuscleGroup.TRICEPS,
        "https://www.muscleandstrength.com/exercises/close-grip-barbell-bench-press.html",
        False,
        None,
        None,
        None,
    )

    # Legs
    SQUAT = (
        "Squat",
        MuscleGroup.QUADS,
        "https://www.muscleandstrength.com/exercises/barbell-full-squat.html",
        False,
        None,
        None,
        None,
    )
    LEG_PRESS = (
        "Leg Press",
        MuscleGroup.QUADS,
        "https://www.muscleandstrength.com/exercises/leg-press.html",
        False,
        None,
        None,
        None,
    )
    LUNGES = ("Lunges", MuscleGroup.GLUTES, None, False, None, None, None)
    ROMANIAN_DEADLIFT = (
        "Romanian Deadlift",
        MuscleGroup.HAMSTRINGS,
        "https://www.muscleandstrength.com/exercises/romanian-deadlift.html",
        True,
        None,
        None,
        None,
    )
    LEG_CURLS = ("Leg Curls", MuscleGroup.HAMSTRINGS, None, False, None, None, None)
    HIP_THRUST = ("Hip Thrust", MuscleGroup.GLUTES, None, False, None, None, None)
    GOBLET_SQUAT = (
        "Goblet Squat",
        MuscleGroup.QUADS,
        "https://www.muscleandstrength.com/exercises/goblet-squat.html",
        False,
        None,
        None,
        None,
    )
    GOOD_MORNINGS = (
        "Good Mornings",
        MuscleGroup.HAMSTRINGS,
        "https://www.muscleandstrength.com/exercises/good-morning.html",
        False,
        None,
        None,
        None,
    )
    CALF_RAISES = ("Calf Raises", MuscleGroup.CALVES, None, False, None, None, None)
    LEG_EXTENSIONS = (
        "Leg Extensions",
        MuscleGroup.QUADS,
        "https://www.muscleandstrength.com/exercises/leg-extensions.html",
        False,
        None,
        None,
        None,
    )

    # Abs & Core
    CRUNCHES = (
        "Crunches",
        MuscleGroup.ABS,
        "https://www.muscleandstrength.com/exercises/crunches.html",
        False,
        None,
        None,
        None,
    )
    LEG_RAISES = ("Leg Raises", MuscleGroup.ABS, None, False, None, None, None)
    PLANKS = (
        "Planks",
        MuscleGroup.ABS,
        "https://www.muscleandstrength.com/exercises/plank.html",
        False,
        None,
        None,
        None,
    )
    RUSSIAN_TWISTS = (
        "Russian Twists",
        MuscleGroup.OBLIQUES,
        None,
        False,
        None,
        None,
        None,
    )
    HANGING_KNEE_RAISES = (
        "Hanging Knee Raises",
        MuscleGroup.ABS,
        None,
        False,
        None,
        None,
        None,
    )
    AB_WHEEL_ROLLOUT = (
        "Ab Wheel Rollout",
        MuscleGroup.ABS,
        "https://www.muscleandstrength.com/exercises/ab-roller.html",
        False,
        None,
        None,
        None,
    )

    # --- NEWLY ADDED EXERCISES ---
    # Chest
    DECLINE_DUMBBELL_BENCH_PRESS = (
        "Decline Dumbbell Bench Press",
        MuscleGroup.CHEST,
        "https://www.muscleandstrength.com/exercises/decline-dumbbell-bench-press.html",
        False,
        None,
        None,
        None,
    )
    INCLINE_DUMBBELL_BENCH_PRESS = (
        "Incline Dumbbell Bench Press",
        MuscleGroup.CHEST,
        "https://www.muscleandstrength.com/exercises/incline-dumbbell-press.html",
        False,
        None,
        None,
        None,
    )

    # Back
    BENT_OVER_DUMBBELL_ROW = (
        "Bent Over Dumbbell Row",
        MuscleGroup.UPPER_BACK,
        "https://www.muscleandstrength.com/exercises/bent-over-dumbbell-row.html",
        False,
        None,
        None,
        None,
    )
    PULLOWVER = (
        "Pullovers",
        MuscleGroup.LATS,
        "https://www.muscleandstrength.com/exercises/straight-arm-dumbbell-pullover.html",
        True,
        None,
        None,
        None,
    )

    # Shoulders
    SEATED_DUMBBELL_PRESS = (
        "Seated Dumbbell Press",
        MuscleGroup.SHOULDERS,
        "https://www.muscleandstrength.com/exercises/seated-dumbbell-press.html",
        False,
        None,
        None,
        None,
    )
    UPRIGHT_ROW = (
        "Upright Row",
        MuscleGroup.SHOULDERS,
        "https://www.muscleandstrength.com/exercises/upright-barbell-row.html",
        False,
        None,
        None,
        None,
    )

    # Biceps
    INCLINE_DUMBBELL_CURL = (
        "Incline Dumbbell Curl",
        MuscleGroup.BICEPS,
        "https://www.muscleandstrength.com/exercises/incline-dumbbell-curl.html",
        False,
        None,
        None,
        None,
    )

    # Triceps
    BENCH_DIP = (
        "Bench Dip",
        MuscleGroup.TRICEPS,
        "https://www.muscleandstrength.com/exercises/bench-dips.html",
        False,
        None,
        None,
        None,
    )

    # Legs
    BARBELL_HACK_SQUAT = (
        "Barbell Hack Squat",
        MuscleGroup.QUADS,
        "https://www.muscleandstrength.com/exercises/barbell-hack-squat.html",
        False,
        None,
        None,
        None,
    )
    BULGARIAN_SPLIT_SQUAT = (
        "Bulgarian Split Squat",
        MuscleGroup.QUADS,
        "https://www.muscleandstrength.com/exercises/bulgarian-split-squat.html",
        False,
        None,
        None,
        None,
    )
    FRONT_SQUAT = (
        "Front Squat",
        MuscleGroup.QUADS,
        "https://www.muscleandstrength.com/exercises/front-barbell-squat.html",
        False,
        None,
        None,
        None,
    )
    SEATED_CALF_RAISE = (
        "Seated Calf Raise",
        MuscleGroup.CALVES,
        "https://www.muscleandstrength.com/exercises/seated-calf-raise.html",
        False,
        None,
        None,
        None,
    )
    STANDING_CALF_RAISE = (
        "Standing Calf Raise",
        MuscleGroup.CALVES,
        "https://www.muscleandstrength.com/exercises/standing-calf-raises.html",
        False,
        None,
        None,
        None,
    )
    GLUTE_HAM_RAISE = (
        "Glute Ham Raise",
        MuscleGroup.HAMSTRINGS,
        "https://www.muscleandstrength.com/exercises/glute-ham-raise.html",
        False,
        None,
        None,
        None,
    )

    # Abs
    DECLINE_CRUNCH = (
        "Decline Crunch",
        MuscleGroup.ABS,
        "https://www.muscleandstrength.com/exercises/decline-crunch.html",
        False,
        None,
        None,
        None,
    )
    DRAGON_FLAG = (
        "Dragon Flag",
        MuscleGroup.ABS,
        "https://www.muscleandstrength.com/exercises/dragon-flag.html",
        False,
        None,
        None,
        None,
    )
    JACKKNIFE_SIT_UP = (
        "Jackknife Sit-up",
        MuscleGroup.ABS,
        "https://www.muscleandstrength.com/exercises/jackknife-sit-up.html",
        False,
        None,
        None,
        None,
    )

    # Forearms
    FARMERS_WALK = (
        "Farmer's Walk",
        MuscleGroup.FOREARMS,
        "https://www.muscleandstrength.com/exercises/farmers-walk.html",
        False,
        None,
        None,
        None,
    )
    WRIST_CURL = (
        "Wrist Curl",
        MuscleGroup.FOREARMS,
        "https://www.muscleandstrength.com/exercises/seated-dumbbell-palms-up-wrist-curl.html",
        False,
        None,
        None,
        None,
    )
    REVERSE_WRIST_CURL = (
        "Reverse Wrist Curl",
        MuscleGroup.FOREARMS,
        "https://www.muscleandstrength.com/exercises/seated-dumbbell-palms-down-wrist-curl.html",
        False,
        None,
        None,
        None,
    )

    # Upper Back
    TRIPOD_DUMBBELL_ROW = (
        "Tripod Dumbbell Row",
        MuscleGroup.UPPER_BACK,
        "https://www.muscleandstrength.com/exercises/tripod-dumbbell-row.html",
        False,
        "Dumbbell",
        "Compound",
        None,
    )
    REVERSE_GRIP_BENT_OVER_DUMBBELL_ROW = (
        "Reverse Grip Bent-Over Dumbbell Row",
        MuscleGroup.UPPER_BACK,
        "https://www.muscleandstrength.com/exercises/reverse-grip-bent-over-dumbbell-row.html",
        False,
        "Dumbbell",
        "Compound",
        None,
    )
    MACHINE_ROW = (
        "Machine Row",
        MuscleGroup.UPPER_BACK,
        "https://www.muscleandstrength.com/exercises/machine-row.html",
        False,
        "Machine",
        "Compound",
        None,
    )
    NEUTRAL_GRIP_CHEST_SUPPORTED_DUMBBELL_ROW = (
        "Neutral Grip Chest Supported Dumbbell Row",
        MuscleGroup.UPPER_BACK,
        "https://www.muscleandstrength.com/exercises/neutral-grip-chest-supported-dumbbell-row.html",
        False,
        "Dumbbell",
        "Compound",
        None,
    )
    FEET_ELEVATED_INVERTED_ROW = (
        "Feet Elevated Inverted Row",
        MuscleGroup.UPPER_BACK,
        "https://www.muscleandstrength.com/exercises/feet-elevated-inverted-row.html",
        False,
        "Bodyweight",
        "Compound",
        None,
    )
    INCLINE_BENCH_TWO_ARM_DUMBBELL_ROW = (
        "Incline Bench Two Arm Dumbbell Row",
        MuscleGroup.UPPER_BACK,
        "https://www.muscleandstrength.com/exercises/incline-bench-two-arm-dumbbell-row.html",
        False,
        "Dumbbell",
        "Compound",
        None,
    )
    MACHINE_T_BAR_ROW = (
        "Machine T-Bar Row",
        MuscleGroup.UPPER_BACK,
        "https://www.muscleandstrength.com/exercises/machine-t-bar-row.html",
        False,
        "Machine",
        "Compound",
        None,
    )
    SEATED_ROW_ROPE_EXTENSION = (
        "Seated Row (Rope Extension)",
        MuscleGroup.UPPER_BACK,
        "https://www.muscleandstrength.com/exercises/seated-row-rope-extension.html",
        False,
        "Cable",
        "Compound",
        None,
    )
    REVERSE_GRIP_BENT_OVER_ROW = (
        "Reverse Grip Bent Over Row",
        MuscleGroup.UPPER_BACK,
        "https://www.muscleandstrength.com/exercises/reverse-grip-bent-over-row.html",
        False,
        "Barbell",
        "Compound",
        None,
    )
    PENDLAY_ROW = (
        "Pendlay Row",
        MuscleGroup.UPPER_BACK,
        "https://www.muscleandstrength.com/exercises/pendlay-row.html",
        False,
        "Barbell",
        "Compound",
        None,
    )
    SMITH_MACHINE_BENT_OVER_ROW = (
        "Smith Machine Bent-Over Row",
        MuscleGroup.UPPER_BACK,
        "https://www.muscleandstrength.com/exercises/smith-machine-bent-over-row.html",
        False,
        "Machine",
        "Compound",
        None,
    )
    INVERTED_ROW = (
        "Inverted Row",
        MuscleGroup.UPPER_BACK,
        "https://www.muscleandstrength.com/exercises/inverted-row.html",
        False,
        "Bodyweight",
        "Compound",
        None,
    )
    RENEGADE_ROW = (
        "Renegade Row",
        MuscleGroup.UPPER_BACK,
        "https://www.muscleandstrength.com/exercises/renegade-row.html",
        False,
        "Dumbbell",
        "Compound",
        None,
    )
    BENT_OVER_KETTLEBELL_ROW = (
        "Bent Over Kettlebell Row",
        MuscleGroup.UPPER_BACK,
        "https://www.muscleandstrength.com/exercises/bent-over-kettlebell-row.html",
        False,
        "Kettlebell",
        "Compound",
        None,
    )
    ONE_ARM_LANDMINE_ROW = (
        "One-Arm Landmine Row",
        MuscleGroup.UPPER_BACK,
        "https://www.muscleandstrength.com/exercises/one-arm-landmine-row.html",
        False,
        "Barbell",
        "Compound",
        None,
    )
    CHEST_SUPPORTED_DUMBBELL_ROW_WITH_ISOHOLD = (
        "Chest Supported Dumbbell Row with Isohold",
        MuscleGroup.UPPER_BACK,
        "https://www.muscleandstrength.com/exercises/chest-supported-dumbbell-row-with-isohold.html",
        False,
        "Dumbbell",
        "Compound",
        None,
    )
    MEADOWS_ROW = (
        "Meadows Row",
        MuscleGroup.UPPER_BACK,
        "https://www.muscleandstrength.com/exercises/meadows-row.html",
        False,
        "Landmine",
        "Compound",
        None,
    )
    ONE_ARM_SEATED_CABLE_ROW = (
        "One-Arm Seated Cable Row",
        MuscleGroup.UPPER_BACK,
        "https://www.muscleandstrength.com/exercises/one-arm-seated-cable-row.html",
        False,
        "Cable",
        "Compound",
        None,
    )
    REVERSE_GRIP_INCLINE_BENCH_TWO_ARM_DUMBBELL_ROW = (
        "Reverse Grip Incline Bench Two-Arm Dumbbell Row",
        MuscleGroup.UPPER_BACK,
        "https://www.muscleandstrength.com/exercises/reverse-grip-incline-bench-two-arm-dumbbell-row.html",
        False,
        "Dumbbell",
        "Compound",
        None,
    )
    INCLINE_BENCH_CABLE_ROW_ROPE_EXTENSION = (
        "Incline Bench Cable Row (Rope Extension)",
        MuscleGroup.UPPER_BACK,
        "https://www.muscleandstrength.com/exercises/incline-bench-cable-row-rope-extension.html",
        False,
        "Cable",
        "Compound",
        None,
    )
    PALM_ROTATIONAL_ROW = (
        "Palm Rotational Row",
        MuscleGroup.UPPER_BACK,
        "https.muscleandstrength.com/exercises/palm-rotational-row.html",
        False,
        "Dumbbell",
        "Compound",
        None,
    )
    ONE_ARM_MACHINE_ROW = (
        "One-Arm Machine Row",
        MuscleGroup.UPPER_BACK,
        "https://www.muscleandstrength.com/exercises/one-arm-machine-row.html",
        False,
        "Machine",
        "Compound",
        None,
    )
    INCLINE_BENCH_BARBELL_ROW = (
        "Incline Bench Barbell Row",
        MuscleGroup.UPPER_BACK,
        "https://www.muscleandstrength.com/exercises/incline-bench-barbell-row.html",
        False,
        "Barbell",
        "Compound",
        None,
    )
    REVERSE_GRIP_SMITH_MACHINE_BENT_OVER_ROW = (
        "Reverse Grip Smith Machine Bent-Over Row",
        MuscleGroup.UPPER_BACK,
        "https://www.muscleandstrength.com/exercises/reverse-grip-smith-machine-bent-over-row.html",
        False,
        "Machine",
        "Compound",
        None,
    )
    DEADSTOP_RACK_ROW = (
        "Deadstop Rack Row",
        MuscleGroup.UPPER_BACK,
        "https://www.muscleandstrength.com/exercises/deadstop-rack-row.html",
        False,
        "Barbell",
        "Compound",
        None,
    )
    SEATED_HIGH_CABLE_ROW = (
        "Seated High Cable Row",
        MuscleGroup.UPPER_BACK,
        "https://www.muscleandstrength.com/exercises/seated-high-cable-row.html",
        False,
        "Cable",
        "Compound",
        None,
    )
    REVERSE_GRIP_BENT_OVER_ROW_EZ_BAR = (
        "Reverse Grip Bent-Over Row (EZ Bar)",
        MuscleGroup.UPPER_BACK,
        "https://www.muscleandstrength.com/exercises/reverse-grip-bent-over-row-ez-bar.html",
        False,
        "EZ Bar",
        "Compound",
        None,
    )

    CABLE_PALM_ROTATIONAL_ROW = (
        "Cable Palm Rotational Row",
        MuscleGroup.UPPER_BACK,
        "https://www.muscleandstrength.com/exercises/cable-palm-rotational-row.html",
        False,
        "Cable",
        "Compound",
        None,
    )
    REVERSE_GRIP_INCLINE_BENCH_BARBELL_ROW = (
        "Reverse Grip Incline Bench Barbell Row",
        MuscleGroup.UPPER_BACK,
        "https://www.muscleandstrength.com/exercises/reverse-grip-incline-bench-barbell-row.html",
        False,
        "Barbell",
        "Compound",
        None,
    )

    # Forearms
    SEATED_BARBELL_WRIST_CURL = (
        "Seated Barbell Wrist Curl",
        MuscleGroup.FOREARMS,
        "https://www.muscleandstrength.com/exercises/seated-barbell-wrist-curl.html",
        False,
        "Barbell",
        "Isolation",
        None,
    )
    PLATE_PINCH_CARRY = (
        "Plate Pinch Carry",
        MuscleGroup.FOREARMS,
        "https://www.muscleandstrength.com/exercises/plate-pinch-carry.html",
        False,
        "Other",
        "Isolation",
        None,
    )
    REVERSE_GRIP_BARBELL_CURL_EZ_BAR = (
        "Reverse Grip Barbell Curl (EZ Bar)",
        MuscleGroup.FOREARMS,
        "https://www.muscleandstrength.com/exercises/reverse-grip-barbell-curl-ez-bar.html",
        False,
        "EZ Bar",
        "Isolation",
        None,
    )
    KETTLEBELL_GOBLET_CARRY = (
        "Kettlebell Goblet Carry",
        MuscleGroup.FOREARMS,
        "https://www.muscleandstrength.com/exercises/kettlebell-goblet-carry.html",
        False,
        "Kettlebell",
        "Compound",
        None,
    )
    SEATED_NEUTRAL_GRIP_DUMBBELL_WRIST_CURL = (
        "Seated Neutral Grip Dumbbell Wrist Curl",
        MuscleGroup.FOREARMS,
        "https://www.muscleandstrength.com/exercises/seated-neutral-grip-dumbbell-wrist-curl.html",
        False,
        "Dumbbell",
        "Isolation",
        None,
    )
    SEATED_CABLE_WRIST_CURL = (
        "Seated Cable Wrist Curl",
        MuscleGroup.FOREARMS,
        "https://www.muscleandstrength.com/exercises/seated-cable-wrist-curl.html",
        False,
        "Cable",
        "Isolation",
        None,
    )
    SMITH_MACHINE_SEATED_WRIST_CURL = (
        "Smith Machine Seated Wrist Curl",
        MuscleGroup.FOREARMS,
        "https://www.muscleandstrength.com/exercises/smith-machine-seated-wrist-curl.html",
        False,
        "Machine",
        "Isolation",
        None,
    )
    KETTLEBELL_RACKED_CROSSOVER_WALK = (
        "Kettlebell Racked Crossover Walk",
        MuscleGroup.FOREARMS,
        "https://www.muscleandstrength.com/exercises/kettlebell-racked-crossover-walk.html",
        False,
        "Kettlebell",
        "Compound",
        None,
    )
    ONE_ARM_SEATED_DUMBBELL_WRIST_CURL = (
        "One-Arm Seated Dumbbell Wrist Curl",
        MuscleGroup.FOREARMS,
        "https://www.muscleandstrength.com/exercises/one-arm-seated-dumbbell-wrist-curl.html",
        False,
        "Dumbbell",
        "Isolation",
        None,
    )
    SEATED_REVERSE_GRIP_CABLE_WRIST_CURL = (
        "Seated Reverse Grip Cable Wrist Curl",
        MuscleGroup.FOREARMS,
        "https://www.muscleandstrength.com/exercises/seated-reverse-grip-cable-wrist-curl.html",
        False,
        "Cable",
        "Isolation",
        None,
    )
    ONE_ARM_REVERSE_DUMBBELL_WRIST_CURL_OVER_BENCH = (
        "One Arm Reverse Dumbbell Wrist Curl Over Bench",
        MuscleGroup.FOREARMS,
        "https://www.muscleandstrength.com/exercises/one-arm-reverse-dumbbell-wrist-curl-over-bench.html",
        False,
        "Dumbbell",
        "Isolation",
        None,
    )
    REVERSE_ONE_ARM_CABLE_CURL = (
        "Reverse One-Arm Cable Curl",
        MuscleGroup.FOREARMS,
        "https://www.muscleandstrength.com/exercises/reverse-one-arm-cable-curl.html",
        False,
        "Cable",
        "Isolation",
        None,
    )
    KETTLEBELL_SINGLE_ARM_BOTTOMS_UP_CARRY = (
        "Kettlebell Single Arm Bottoms Up Carry",
        MuscleGroup.FOREARMS,
        "https://www.muscleandstrength.com/exercises/kettlebell-single-arm-bottoms-up-carry.html",
        False,
        "Kettlebell",
        "Compound",
        None,
    )
    ONE_ARM_SEATED_NEUTRAL_GRIP_DUMBBELL_WRIST_CURL = (
        "One-Arm Seated Neutral Grip Dumbbell Wrist Curl",
        MuscleGroup.FOREARMS,
        "https://www.muscleandstrength.com/exercises/one-arm-seated-neutral-grip-dumbbell-wrist-curl.html",
        False,
        "Dumbbell",
        "Isolation",
        None,
    )
    REVERSE_GRIP_CABLE_CURL = (
        "Reverse Grip Cable Curl",
        MuscleGroup.FOREARMS,
        "https://www.muscleandstrength.com/exercises/reverse-grip-cable-curl.html",
        False,
        "Cable",
        "Isolation",
        None,
    )
    STANDING_SMITH_MACHINE_WRIST_CURL_BEHIND_BACK = (
        "Standing Smith Machine Wrist Curl (behind back)",
        MuscleGroup.FOREARMS,
        "https://www.muscleandstrength.com/exercises/standing-smith-machine-wrist-curl-behind-back.html",
        False,
        "Machine",
        "Isolation",
        None,
    )
    BEHIND_THE_BACK_BARBELL_WRIST_CURL = (
        "Behind-The-Back Barbell Wrist Curl",
        MuscleGroup.FOREARMS,
        "https://www.muscleandstrength.com/exercises/behind-the-back-barbell-wrist-curl.html",
        False,
        "Barbell",
        "Isolation",
        None,
    )
    KETTLEBELL_SINGLE_ARM_RACKED_CARRY = (
        "Kettlebell Single Arm Racked Carry",
        MuscleGroup.FOREARMS,
        "https://www.muscleandstrength.com/exercises/kettlebell-single-arm-racked-carry.html",
        False,
        "Kettlebell",
        "Compound",
        None,
    )
    NEUTRAL_GRIP_DUMBBELL_WRIST_CURL_OVER_BENCH = (
        "Neutral Grip Dumbbell Wrist Curl (Over Bench)",
        MuscleGroup.FOREARMS,
        "https://www.muscleandstrength.com/exercises/neutral-grip-dumbbell-wrist-curl-over-bench.html",
        False,
        "Dumbbell",
        "Isolation",
        None,
    )
    STANDING_REVERSE_GRIP_CABLE_CURL = (
        "Standing Reverse Grip Cable Curl",
        MuscleGroup.FOREARMS,
        "https://www.muscleandstrength.com/exercises/standing-reverse-grip-cable-curl.html",
        False,
        "Cable",
        "Isolation",
        None,
    )
    WEIGHT_PLATE_PINCHES = (
        "Weight Plate Pinches",
        MuscleGroup.FOREARMS,
        "https://www.muscleandstrength.com/exercises/weight-plate-pinches.html",
        False,
        "Other",
        "Isolation",
        None,
    )
    REVERSE_GRIP_BARBELL_CURL = (
        "Reverse Grip Barbell Curl",
        MuscleGroup.FOREARMS,
        "https://www.muscleandstrength.com/exercises/reverse-grip-barbell-curl.html",
        False,
        "Barbell",
        "Isolation",
        None,
    )
    OVERHEAD_BARBELL_CARRY = (
        "Overhead Barbell Carry",
        MuscleGroup.FOREARMS,
        "https://www.muscleandstrength.com/exercises/overhead-barbell-carry.html",
        False,
        "Barbell",
        "Compound",
        None,
    )
    ONE_ARM_SEATED_REVERSE_GRIP_DUMBBELL_WRIST_CURL = (
        "One-Arm Seated Reverse Grip Dumbbell Wrist Curl",
        MuscleGroup.FOREARMS,
        "https://www.muscleandstrength.com/exercises/one-arm-seated-reverse-grip-dumbbell-wrist-curl.html",
        False,
        "Dumbbell",
        "Isolation",
        None,
    )
    WRIST_ROLLERS = (
        "Wrist Rollers",
        MuscleGroup.FOREARMS,
        "https://www.muscleandstrength.com/exercises/wrist-rollers.html",
        False,
        "Other",
        "Isolation",
        None,
    )
    DUMBBELL_FARMERS_CARRY = (
        "Dumbbell Farmers Carry",
        MuscleGroup.FOREARMS,
        "https://www.muscleandstrength.com/exercises/dumbbell-farmers-carry.html",
        False,
        "Dumbbell",
        "Compound",
        None,
    )
    REVERSE_GRIP_PREACHER_CURL_EZ_BAR = (
        "Reverse Grip Preacher Curl (EZ Bar)",
        MuscleGroup.FOREARMS,
        "https://www.muscleandstrength.com/exercises/reverse-grip-preacher-curl-ez-bar.html",
        False,
        "EZ Bar",
        "Isolation",
        None,
    )
    TRAP_BAR_FARMERS_CARRY = (
        "Trap Bar Farmers Carry",
        MuscleGroup.FOREARMS,
        "https://www.muscleandstrength.com/exercises/trap-bar-farmers-carry.html",
        False,
        "Other",
        "Compound",
        None,
    )
    SEATED_DUMBBELL_WRIST_CURL = (
        "Seated Dumbbell Wrist Curl",
        MuscleGroup.FOREARMS,
        "https://www.muscleandstrength.com/exercises/seated-dumbbell-wrist-curl.html",
        False,
        "Dumbbell",
        "Isolation",
        None,
    )
    REVERSE_GRIP_CONCENTRATION_CURL = (
        "Reverse Grip Concentration Curl",
        MuscleGroup.FOREARMS,
        "https://www.muscleandstrength.com/exercises/reverse-grip-concentration-curl.html",
        False,
        "Dumbbell",
        "Isolation",
        None,
    )
    BARBELL_SUITCASE_CARRY = (
        "Barbell Suitcase Carry",
        MuscleGroup.FOREARMS,
        "https://www.muscleandstrength.com/exercises/barbell-suitcase-carry.html",
        False,
        "Barbell",
        "Compound",
        None,
    )
    BARBELL_WRIST_CURL_OVER_BENCH = (
        "Barbell Wrist Curl (Over Bench)",
        MuscleGroup.FOREARMS,
        "https://www.muscleandstrength.com/exercises/barbell-wrist-curl-over-bench.html",
        False,
        "Barbell",
        "Isolation",
        None,
    )
    TRAP_BAR_OVERHEAD_CARRY = (
        "Trap Bar Overhead Carry",
        MuscleGroup.FOREARMS,
        "https://www.muscleandstrength.com/exercises/trap-bar-overhead-carry.html",
        False,
        "Other",
        "Compound",
        None,
    )
    DUMBBELL_WRIST_CURL_OVER_BENCH = (
        "Dumbbell Wrist Curl (Over Bench)",
        MuscleGroup.FOREARMS,
        "https://www.muscleandstrength.com/exercises/dumbbell-wrist-curl-over-bench.html",
        False,
        "Dumbbell",
        "Isolation",
        None,
    )
    ONE_ARM_DUMBBELL_WRIST_CURL_OVER_BENCH = (
        "One-Arm Dumbbell Wrist Curl (Over Bench)",
        MuscleGroup.FOREARMS,
        "https://www.muscleandstrength.com/exercises/one-arm-dumbbell-wrist-curl-over-bench.html",
        False,
        "Dumbbell",
        "Isolation",
        None,
    )
    FAT_GRIPZ_DUMBBELL_FARMERS_CARRY = (
        "Fat Gripz Dumbbell Farmers Carry",
        MuscleGroup.FOREARMS,
        "https://www.muscleandstrength.com/exercises/fat-gripz-dumbbell-farmers-carry.html",
        False,
        "Dumbbell",
        "Compound",
        None,
    )
    REVERSE_GRIP_BARBELL_WRIST_CURL_OVER_BENCH = (
        "Reverse Grip Barbell Wrist Curl (Over Bench)",
        MuscleGroup.FOREARMS,
        "https://www.muscleandstrength.com/exercises/reverse-grip-barbell-wrist-curl-over-bench.html",
        False,
        "Barbell",
        "Isolation",
        None,
    )
    ONE_ARM_DUMBBELL_REVERSE_GRIP_CURL = (
        "One-Arm Dumbbell Reverse Grip Curl",
        MuscleGroup.FOREARMS,
        "https://www.muscleandstrength.com/exercises/one-arm-dumbbell-reverse-grip-curl.html",
        False,
        "Dumbbell",
        "Isolation",
        None,
    )
    ZERCHER_CARRY = (
        "Zercher Carry",
        MuscleGroup.FOREARMS,
        "https://www.muscleandstrength.com/exercises/zercher-carry.html",
        False,
        "Barbell",
        "Compound",
        None,
    )
    ONE_ARM_NEUTRAL_GRIP_DUMBBELL_WRIST_CURL_OVER_BENCH = (
        "One-Arm Neutral Grip Dumbbell Wrist Curl (Over Bench)",
        MuscleGroup.FOREARMS,
        "https://www.muscleandstrength.com/exercises/one-arm-neutral-grip-dumbbell-wrist-curl-over-bench.html",
        False,
        "Dumbbell",
        "Isolation",
        None,
    )

    # Lats
    CLOSE_GRIP_LAT_PULL_DOWN = (
        "Close Grip Lat Pull Down",
        MuscleGroup.LATS,
        "https://www.muscleandstrength.com/exercises/close-grip-lat-pull-down.html",
        False,
        "Cable",
        "Compound",
        None,
    )
    WIDE_GRIP_PULL_UP = (
        "Wide Grip Pull Up",
        MuscleGroup.LATS,
        "https://www.muscleandstrength.com/exercises/wide-grip-pull-up.html",
        False,
        "Bodyweight",
        "Compound",
        None,
    )
    STRAIGHT_ARM_LAT_PULL_DOWN = (
        "Straight Arm Lat Pull Down",
        MuscleGroup.LATS,
        "https://www.muscleandstrength.com/exercises/straight-arm-lat-pull-down.html",
        False,
        "Cable",
        "Isolation",
        None,
    )
    CHIN_UP = (
        "Chin Up",
        MuscleGroup.LATS,
        "https://www.muscleandstrength.com/exercises/chin-up.html",
        False,
        "Bodyweight",
        "Compound",
        None,
    )
    WIDE_GRIP_LAT_PULL_DOWN = (
        "Wide Grip Lat Pull Down",
        MuscleGroup.LATS,
        "https://www.muscleandstrength.com/exercises/wide-grip-lat-pull-down.html",
        False,
        "Cable",
        "Compound",
        None,
    )
    REVERSE_GRIP_LAT_PULL_DOWN_UNDERHAND = (
        "Reverse Grip Lat Pull Down (Underhand)",
        MuscleGroup.LATS,
        "https://www.muscleandstrength.com/exercises/reverse-grip-lat-pull-down-underhand.html",
        False,
        "Cable",
        "Compound",
        None,
    )
    ROPE_STRAIGHT_ARM_PULL_DOWN = (
        "Rope Straight Arm Pull Down",
        MuscleGroup.LATS,
        "https://www.muscleandstrength.com/exercises/rope-straight-arm-pull-down.html",
        False,
        "Cable",
        "Isolation",
        None,
    )
    V_BAR_PULL_UP = (
        "V-Bar Pull Up",
        MuscleGroup.LATS,
        "https://www.muscleandstrength.com/exercises/v-bar-pull-up.html",
        False,
        "Bodyweight",
        "Compound",
        None,
    )
    V_BAR_PULL_DOWN = (
        "V-Bar Pull Down",
        MuscleGroup.LATS,
        "https://www.muscleandstrength.com/exercises/v-bar-pull-down.html",
        False,
        "Cable",
        "Compound",
        None,
    )
    CLOSE_GRIP_PULL_UP = (
        "Close Grip Pull Up",
        MuscleGroup.LATS,
        "https://www.muscleandstrength.com/exercises/close-grip-pull-up.html",
        False,
        "Bodyweight",
        "Compound",
        None,
    )
    SHOTGUN_ROW = (
        "Shotgun Row",
        MuscleGroup.LATS,
        "https://www.muscleandstrength.com/exercises/shotgun-row.html",
        False,
        "Cable",
        "Compound",
        None,
    )
    WEIGHTED_PULL_UP = (
        "Weighted Pull Up",
        MuscleGroup.LATS,
        "https://www.muscleandstrength.com/exercises/weighted-pull-up.html",
        False,
        "Other",
        "Compound",
        None,
    )
    RACK_LAT_STRETCH = (
        "Rack Lat Stretch",
        MuscleGroup.LATS,
        "https://www.muscleandstrength.com/exercises/rack-lat-stretch.html",
        False,
        "Other",
        "Isolation",
        None,
    )
    WEIGHTED_CHIN_UP = (
        "Weighted Chin Up",
        MuscleGroup.LATS,
        "https://www.muscleandstrength.com/exercises/weighted-chin-up.html",
        False,
        "Other",
        "Compound",
        None,
    )
    ECCENTRIC_ONLY_PULL_UP = (
        "Eccentric Only Pull Up",
        MuscleGroup.LATS,
        "https://www.muscleandstrength.com/exercises/eccentric-only-pull-up.html",
        False,
        "Bodyweight",
        "Compound",
        None,
    )
    BEHIND_NECK_LAT_PULL_DOWN = (
        "Behind Neck Lat Pull Down",
        MuscleGroup.LATS,
        "https://www.muscleandstrength.com/exercises/behind-neck-lat-pull-down.html",
        False,
        "Cable",
        "Compound",
        None,
    )
    RESISTANCE_BAND_ASSISTED_PULL_UP_FROM_FOOT = (
        "Resistance Band Assisted Pull Up (From Foot)",
        MuscleGroup.LATS,
        "https://www.muscleandstrength.com/exercises/resistance-band-assisted-pull-up-from-foot.html",
        False,
        "Band",
        "Compound",
        None,
    )
    RESISTANCE_BAND_ASSISTED_PULL_UP_FROM_KNEE = (
        "Resistance Band Assisted Pull Up (From Knee)",
        MuscleGroup.LATS,
        "https://www.muscleandstrength.com/exercises/resistance-band-assisted-pull-up-from-knee.html",
        False,
        "Band",
        "Compound",
        None,
    )
    CLOSE_GRIP_CHIN_UP = (
        "Close Grip Chin Up",
        MuscleGroup.LATS,
        "https://www.muscleandstrength.com/exercises/close-grip-chin-up.html",
        False,
        "Bodyweight",
        "Compound",
        None,
    )
    STANDING_OVERHEAD_MEDICINE_BALL_THROW = (
        "Standing Overhead Medicine Ball Throw",
        MuscleGroup.LATS,
        "https://www.muscleandstrength.com/exercises/standing-overhead-medicine-ball-throw.html",
        False,
        "Medicine Ball",
        "Compound",
        None,
    )
    LATERAL_PULLDOWN_ROPE_EXTENSION = (
        "Lateral Pulldown (Rope Extension)",
        MuscleGroup.LATS,
        "https://www.muscleandstrength.com/exercises/lateral-pulldown-rope-extension.html",
        False,
        "Cable",
        "Compound",
        None,
    )
    UNDERHAND_CLOSE_GRIP_LATERAL_PULLDOWN = (
        "Underhand Close Grip Lateral Pulldown",
        MuscleGroup.LATS,
        "https://www.muscleandstrength.com/exercises/underhand-close-grip-lateral-pulldown.html",
        False,
        "Cable",
        "Compound",
        None,
    )
    BAND_ASSISTED_CHIN_UP_FROM_FOOT = (
        "Band Assisted Chin Up (From Foot)",
        MuscleGroup.LATS,
        "https://www.muscleandstrength.com/exercises/band-assisted-chin-up-from-foot.html",
        False,
        "Band",
        "Compound",
        None,
    )
    WIDE_GRIP_CHIN_UP = (
        "Wide Grip Chin Up",
        MuscleGroup.LATS,
        "https://www.muscleandstrength.com/exercises/wide-grip-chin-up.html",
        False,
        "Bodyweight",
        "Compound",
        None,
    )
    PULL_UP_WITH_LEG_RAISE = (
        "Pull Up with Leg Raise",
        MuscleGroup.LATS,
        "https://www.muscleandstrength.com/exercises/pull-up-with-leg-raise.html",
        False,
        "Bodyweight",
        "Compound",
        None,
    )
    ROPE_CLIMB = (
        "Rope Climb",
        MuscleGroup.LATS,
        "https://www.muscleandstrength.com/exercises/rope-climb.html",
        False,
        "Other",
        "Compound",
        None,
    )
    ARMS_ONLY_ROPE_CLIMB = (
        "Arms Only Rope Climb",
        MuscleGroup.LATS,
        "https://www.muscleandstrength.com/exercises/arms-only-rope-climb.html",
        False,
        "Other",
        "Compound",
        None,
    )
    L_SIT_PULL_UP = (
        "L-Sit Pull Up",
        MuscleGroup.LATS,
        "https://www.muscleandstrength.com/exercises/l-sit-pull-up.html",
        False,
        "Bodyweight",
        "Compound",
        None,
    )
    ARCHER_PULL_UP = (
        "Archer Pull Up",
        MuscleGroup.LATS,
        "https://www.muscleandstrength.com/exercises/archer-pull-up.html",
        False,
        "Bodyweight",
        "Compound",
        None,
    )
    THIBAUDEAU_KAYAK_ROW = (
        "Thibaudeau Kayak Row",
        MuscleGroup.LATS,
        "https://www.muscleandstrength.com/exercises/thibaudeau-kayak-row.html",
        False,
        "Cable",
        "Compound",
        None,
    )
    STANDING_OVERHEAD_MEDICINE_BALL_SLAM = (
        "Standing Overhead Medicine Ball Slam",
        MuscleGroup.LATS,
        "https://www.muscleandstrength.com/exercises/standing-overhead-medicine-ball-slam.html",
        False,
        "Medicine Ball",
        "Compound",
        None,
    )
    ECCENTRIC_ONLY_CHIN_UP = (
        "Eccentric Only Chin Up",
        MuscleGroup.LATS,
        "https://www.muscleandstrength.com/exercises/eccentric-only-chin-up.html",
        False,
        "Bodyweight",
        "Compound",
        None,
    )
    BAND_RESISTED_CHIN_UP = (
        "Band Resisted Chin Up",
        MuscleGroup.LATS,
        "https://www.muscleandstrength.com/exercises/band-resisted-chin-up.html",
        False,
        "Band",
        "Compound",
        None,
    )
    WEIGHTED_PULL_UP_HANG = (
        "Weighted Pull Up Hang",
        MuscleGroup.LATS,
        "https://www.muscleandstrength.com/exercises/weighted-pull-up-hang.html",
        False,
        "Other",
        "Compound",
        None,
    )
    ONE_ARM_CHIN_UP = (
        "One Arm Chin Up",
        MuscleGroup.LATS,
        "https://www.muscleandstrength.com/exercises/one-arm-chin-up.html",
        False,
        "Bodyweight",
        "Compound",
        None,
    )
    GIRONDA_STERNUM_CHIN_UP = (
        "Gironda Sternum Chin Up",
        MuscleGroup.LATS,
        "https://www.muscleandstrength.com/exercises/gironda-sternum-chin-up.html",
        False,
        "Bodyweight",
        "Compound",
        None,
    )
    MIXED_GRIP_CHIN_UP = (
        "Mixed Grip Chin Up",
        MuscleGroup.LATS,
        "https://www.muscleandstrength.com/exercises/mixed-grip-chin-up.html",
        False,
        "Bodyweight",
        "Compound",
        None,
    )
    SINGLE_LEG_OVERHEAD_MEDICINE_BALL_TAP = (
        "Single Leg Overhead Medicine Ball Tap",
        MuscleGroup.LATS,
        "https://www.muscleandstrength.com/exercises/single-leg-overhead-medicine-ball-tap.html",
        False,
        "Medicine Ball",
        "Compound",
        None,
    )

    # Shoulders
    BENT_OVER_LOW_PULLEY_REAR_DELT_FLY = (
        "Bent Over Low Pulley Rear Delt Fly",
        MuscleGroup.SHOULDERS,
        "https://www.muscleandstrength.com/exercises/bent-over-low-pulley-rear-delt-fly.html",
        False,
        "Cable",
        "Isolation",
        None,
    )
    SMITH_MACHINE_SHOULDER_PRESS = (
        "Smith Machine Shoulder Press",
        MuscleGroup.SHOULDERS,
        "https://www.muscleandstrength.com/exercises/smith-machine-shoulder-press.html",
        False,
        "Machine",
        "Compound",
        None,
    )
    SEATED_BENT_OVER_DUMBBELL_REVERSE_FLY = (
        "Seated Bent Over Dumbbell Reverse Fly",
        MuscleGroup.SHOULDERS,
        "https://www.muscleandstrength.com/exercises/seated-bent-over-dumbbell-reverse-fly.html",
        False,
        "Dumbbell",
        "Isolation",
        None,
    )
    SEATED_DUMBBELL_LATERAL_RAISE = (
        "Seated Dumbbell Lateral Raise",
        MuscleGroup.SHOULDERS,
        "https://www.muscleandstrength.com/exercises/seated-dumbbell-lateral-raise.html",
        False,
        "Dumbbell",
        "Isolation",
        None,
    )
    STANDING_CABLE_REVERSE_FLY = (
        "Standing Cable Reverse Fly",
        MuscleGroup.SHOULDERS,
        "https://www.muscleandstrength.com/exercises/standing-cable-reverse-fly.html",
        False,
        "Cable",
        "Isolation",
        None,
    )
    SEATED_BARBELL_SHOULDER_PRESS = (
        "Seated Barbell Shoulder Press",
        MuscleGroup.SHOULDERS,
        "https://www.muscleandstrength.com/exercises/seated-barbell-shoulder-press.html",
        False,
        "Barbell",
        "Compound",
        None,
    )
    MACHINE_REVERSE_FLY = (
        "Machine Reverse Fly",
        MuscleGroup.SHOULDERS,
        "https://www.muscleandstrength.com/exercises/machine-reverse-fly.html",
        False,
        "Machine",
        "Isolation",
        None,
    )
    MACHINE_SHOULDER_PRESS = (
        "Machine Shoulder Press",
        MuscleGroup.SHOULDERS,
        "https://www.muscleandstrength.com/exercises/machine-shoulder-press.html",
        False,
        "Machine",
        "Compound",
        None,
    )
    SINGLE_ARM_CABLE_LATERAL_RAISE_CROSSBODY = (
        "Single Arm Cable Lateral Raise (Crossbody)",
        MuscleGroup.SHOULDERS,
        "https://www.muscleandstrength.com/exercises/single-arm-cable-lateral-raise-crossbody.html",
        False,
        "Cable",
        "Isolation",
        None,
    )
    CABLE_LATERAL_RAISE = (
        "Cable Lateral Raise",
        MuscleGroup.SHOULDERS,
        "https://www.muscleandstrength.com/exercises/cable-lateral-raise.html",
        False,
        "Cable",
        "Isolation",
        None,
    )
    SEATED_BEHIND_THE_NECK_SHOULDER_PRESS = (
        "Seated Behind the Neck Shoulder Press",
        MuscleGroup.SHOULDERS,
        "https://www.muscleandstrength.com/exercises/seated-behind-the-neck-shoulder-press.html",
        False,
        "Barbell",
        "Compound",
        None,
    )
    CABLE_UPRIGHT_ROW = (
        "Cable Upright Row",
        MuscleGroup.SHOULDERS,
        "https://www.muscleandstrength.com/exercises/cable-upright-row.html",
        False,
        "Cable",
        "Compound",
        None,
    )
    SMITH_MACHINE_UPRIGHT_ROW = (
        "Smith Machine Upright Row",
        MuscleGroup.SHOULDERS,
        "https://www.muscleandstrength.com/exercises/smith-machine-upright-row.html",
        False,
        "Machine",
        "Compound",
        None,
    )
    LATERAL_RAISE_MACHINE = (
        "Lateral Raise Machine",
        MuscleGroup.SHOULDERS,
        "https://www.muscleandstrength.com/exercises/lateral-raise-machine.html",
        False,
        "Machine",
        "Isolation",
        None,
    )
    BAND_PULL_APART = (
        "Band Pull Apart",
        MuscleGroup.SHOULDERS,
        "https://www.muscleandstrength.com/exercises/band-pull-apart.html",
        False,
        "Band",
        "Isolation",
        None,
    )
    BENT_OVER_REAR_DELT_FLY_HEAD_ON_BENCH = (
        "Bent Over Rear Delt Fly (Head on Bench)",
        MuscleGroup.SHOULDERS,
        "https://www.muscleandstrength.com/exercises/bent-over-rear-delt-fly-head-on-bench.html",
        False,
        "Dumbbell",
        "Isolation",
        None,
    )
    ONE_ARM_DUMBBELL_LATERAL_RAISE = (
        "One-Arm Dumbbell Lateral Raise",
        MuscleGroup.SHOULDERS,
        "https://www.muscleandstrength.com/exercises/one-arm-dumbbell-lateral-raise.html",
        False,
        "Dumbbell",
        "Isolation",
        None,
    )
    SCAPULAR_WALL_SLIDE = (
        "Scapular Wall Slide",
        MuscleGroup.SHOULDERS,
        "https://www.muscleandstrength.com/exercises/scapular-wall-slide.html",
        False,
        "Bodyweight",
        "Isolation",
        None,
    )
    HALF_KNEELING_LANDMINE_PRESS = (
        "Half Kneeling Landmine Press",
        MuscleGroup.SHOULDERS,
        "https://www.muscleandstrength.com/exercises/half-kneeling-landmine-press.html",
        False,
        "Landmine",
        "Compound",
        None,
    )
    WEIGHT_PLATE_FRONT_RAISE = (
        "Weight Plate Front Raise",
        MuscleGroup.SHOULDERS,
        "https://www.muscleandstrength.com/exercises/weight-plate-front-raise.html",
        False,
        "Other",
        "Isolation",
        None,
    )
    DUMBBELL_UPRIGHT_ROW = (
        "Dumbbell Upright Row",
        MuscleGroup.SHOULDERS,
        "https://www.muscleandstrength.com/exercises/dumbbell-upright-row.html",
        False,
        "Dumbbell",
        "Compound",
        None,
    )
    INCLINE_REAR_DELT_FLY = (
        "Incline Rear Delt Fly",
        MuscleGroup.SHOULDERS,
        "https://www.muscleandstrength.com/exercises/incline-rear-delt-fly.html",
        False,
        "Dumbbell",
        "Isolation",
        None,
    )
    STANDING_ARNOLD_PRESS = (
        "Standing Arnold Press",
        MuscleGroup.SHOULDERS,
        "https://www.muscleandstrength.com/exercises/standing-arnold-press.html",
        False,
        "Dumbbell",
        "Compound",
        None,
    )
    KETTLEBELL_HALO = (
        "Kettlebell Halo",
        MuscleGroup.SHOULDERS,
        "https://www.muscleandstrength.com/exercises/kettlebell-halo.html",
        False,
        "Kettlebell",
        "Isolation",
        None,
    )
    CABLE_EXTERNAL_ROTATION = (
        "Cable External Rotation",
        MuscleGroup.SHOULDERS,
        "https://www.muscleandstrength.com/exercises/cable-external-rotation.html",
        False,
        "Cable",
        "Isolation",
        None,
    )
    CABLE_FRONT_RAISE_BILATERAL = (
        "Cable Front Raise (Bilateral)",
        MuscleGroup.SHOULDERS,
        "https://www.muscleandstrength.com/exercises/cable-front-raise-bilateral.html",
        False,
        "Cable",
        "Isolation",
        None,
    )
    SIDE_LYING_REAR_DELT_FLY = (
        "Side Lying Rear Delt Fly",
        MuscleGroup.SHOULDERS,
        "https://www.muscleandstrength.com/exercises/side-lying-rear-delt-fly.html",
        False,
        "Dumbbell",
        "Isolation",
        None,
    )
    LATERAL_RAISE_PARTIALS = (
        "Lateral Raise Partials",
        MuscleGroup.SHOULDERS,
        "https://www.muscleandstrength.com/exercises/lateral-raise-partials.html",
        False,
        "Dumbbell",
        "Isolation",
        None,
    )
    BANDED_LATERAL_RAISE = (
        "Banded Lateral Raise",
        MuscleGroup.SHOULDERS,
        "https://www.muscleandstrength.com/exercises/banded-lateral-raise.html",
        False,
        "Band",
        "Isolation",
        None,
    )
    CABLE_FACE_PULL_WITH_EXTERNAL_ROTATION = (
        "Cable Face Pull with External Rotation",
        MuscleGroup.SHOULDERS,
        "https://www.muscleandstrength.com/exercises/cable-face-pull-with-external-rotation.html",
        False,
        "Cable",
        "Compound",
        None,
    )
    BARBELL_CLEAN_AND_PRESS = (
        "Barbell Clean and Press",
        MuscleGroup.SHOULDERS,
        "https://www.muscleandstrength.com/exercises/clean-and-press.html",
        False,
        "Barbell",
        "Compound",
        None,
    )

    # Adductors
    HIP_ADDUCTION_MACHINE = (
        "Hip Adduction Machine",
        MuscleGroup.ADDUCTORS,
        "https://www.muscleandstrength.com/exercises/adductors.html",
        False,
        "Machine",
        "Isolation",
        None,
    )
    DEEP_SQUAT_PRYING = (
        "Deep Squat Prying",
        MuscleGroup.ADDUCTORS,
        "https://www.muscleandstrength.com/exercises/adductors.html",
        False,
        "Bodyweight",
        "Compound",
        None,
    )
    ALTERNATING_LATERAL_LUNGE_WITH_OVERHEAD_REACH = (
        "Alternating Lateral Lunge with Overhead Reach",
        MuscleGroup.ADDUCTORS,
        "https://www.muscleandstrength.com/exercises/adductors.html",
        False,
        "Bodyweight",
        "Compound",
        None,
    )
    CABLE_HIP_ADDUCTION = (
        "Cable Hip Adduction",
        MuscleGroup.ADDUCTORS,
        "https://www.muscleandstrength.com/exercises/adductors.html",
        False,
        "Cable",
        "Isolation",
        None,
    )
    ADDUCTOR_FOAM_ROLLING = (
        "Adductor Foam Rolling",
        MuscleGroup.ADDUCTORS,
        "https://www.muscleandstrength.com/exercises/adductors.html",
        False,
        "Other",
        "Isolation",
        None,
    )
    LATERAL_KNEELING_ADDUCTOR_MOBILIZATION = (
        "Lateral Kneeling Adductor Mobilization",
        MuscleGroup.ADDUCTORS,
        "https://www.muscleandstrength.com/exercises/adductors.html",
        False,
        "Bodyweight",
        "Isolation",
        None,
    )
    ROCKING_FROG_STRETCH = (
        "Rocking Frog Stretch",
        MuscleGroup.ADDUCTORS,
        "https://www.muscleandstrength.com/exercises/adductors.html",
        False,
        "Bodyweight",
        "Isolation",
        None,
    )

    # Biceps
    BARBELL_DRAG_CURL = (
        "Barbell Drag Curl",
        MuscleGroup.BICEPS,
        "https://www.muscleandstrength.com/exercises/barbell-drag-curl.html",
        False,
        "Barbell",
        "Isolation",
        None,
    )
    CLOSE_GRIP_STANDING_BARBELL_CURL = (
        "Close Grip Standing Barbell Curl",
        MuscleGroup.BICEPS,
        "https://www.muscleandstrength.com/exercises/close-grip-standing-barbell-curl.html",
        False,
        "Barbell",
        "Isolation",
        None,
    )
    DUMBBELL_HAMMER_PREACHER_CURL = (
        "Dumbbell Hammer Preacher Curl",
        MuscleGroup.BICEPS,
        "https://www.muscleandstrength.com/exercises/dumbbell-hammer-preacher-curl.html",
        False,
        "Dumbbell",
        "Isolation",
        None,
    )
    DUMBBELL_PREACHER_CURL = (
        "Dumbbell Preacher Curl",
        MuscleGroup.BICEPS,
        "https://www.muscleandstrength.com/exercises/dumbbell-preacher-curl.html",
        False,
        "Dumbbell",
        "Isolation",
        None,
    )
    SEATED_ZOTTMAN_CURL = (
        "Seated Zottman Curl",
        MuscleGroup.BICEPS,
        "https://www.muscleandstrength.com/exercises/seated-zottman-curl.html",
        False,
        "Dumbbell",
        "Isolation",
        None,
    )
    STANDING_DUMBBELL_DRAG_CURL = (
        "Standing Dumbbell Drag Curl",
        MuscleGroup.BICEPS,
        "https://www.muscleandstrength.com/exercises/standing-dumbbell-drag-curl.html",
        False,
        "Dumbbell",
        "Isolation",
        None,
    )
    STANDING_DUMBBELL_REVERSE_CURL = (
        "Standing Dumbbell Reverse Curl",
        MuscleGroup.BICEPS,
        "https://www.muscleandstrength.com/exercises/standing-dumbbell-reverse-curl.html",
        False,
        "Dumbbell",
        "Isolation",
        None,
    )
    ZOTTMAN_CURL = (
        "Zottman Curl",
        MuscleGroup.BICEPS,
        "https://www.muscleandstrength.com/exercises/zottman-curl.html",
        False,
        "Dumbbell",
        "Isolation",
        None,
    )

    def __init__(
        self,
        display_name,
        muscle_group,
        url=None,
        is_popular=False,
        equipment_type=None,
        mechanics_type=None,
        my_custom_group=None,
    ):
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


