from models import WorkPlanBase, WorkPlanSummary, WorkPlanScheduleBase, WorkPlanScheduleDay
from enums import MuscleGroup, Exercise

default_plan = WorkPlanBase(
    user_id="default",
    workplan_summary=WorkPlanSummary(
        goal="Muscle & Strength",
        workout_type="Full Body",
        training_level="Beginner",
        program_duration="12 Weeks",
        days_per_week=5,
        time_per_workout="60-90 Mins",
        equipments=["Barbell", "Dumbbell", "Machine", "Cable", "Bodyweight"],
        target_gender="Female",
        recommended_supplements=["Whey Protein", "Creatine", "Fish Oil"]
    ),
    workplan_schedule=WorkPlanScheduleBase(
        id="default_schedule",
        monday=[
            WorkPlanScheduleDay(muscle_group=[MuscleGroup.CHEST.name], exercise=[Exercise.INCLINE_DUMBBELL_BENCH_PRESS.name]),
            WorkPlanScheduleDay(muscle_group=[MuscleGroup.QUADS.name], exercise=[Exercise.BARBELL_HACK_SQUAT.name]),
            WorkPlanScheduleDay(muscle_group=[MuscleGroup.SHOULDERS.name], exercise=[Exercise.SEATED_DUMBBELL_PRESS.name]),
            WorkPlanScheduleDay(muscle_group=[MuscleGroup.UPPER_BACK.name], exercise=[Exercise.BENT_OVER_DUMBBELL_ROW.name]),
            WorkPlanScheduleDay(muscle_group=[MuscleGroup.TRICEPS.name], exercise=[Exercise.BENCH_DIP.name]),
            WorkPlanScheduleDay(muscle_group=[MuscleGroup.BICEPS.name], exercise=[Exercise.INCLINE_DUMBBELL_CURL.name]),
            WorkPlanScheduleDay(muscle_group=[MuscleGroup.CALVES.name], exercise=[Exercise.SEATED_CALF_RAISE.name]),
        ],
        tuesday=[
            WorkPlanScheduleDay(muscle_group=[MuscleGroup.CHEST.name], exercise=[Exercise.DECLINE_DUMBBELL_BENCH_PRESS.name]),
            WorkPlanScheduleDay(muscle_group=[MuscleGroup.QUADS.name], exercise=[Exercise.BULGARIAN_SPLIT_SQUAT.name]),
            WorkPlanScheduleDay(muscle_group=[MuscleGroup.SHOULDERS.name], exercise=[Exercise.UPRIGHT_ROW.name]),
            WorkPlanScheduleDay(muscle_group=[MuscleGroup.LATS.name], exercise=[Exercise.LAT_PULLDOWN.name]),
            WorkPlanScheduleDay(muscle_group=[MuscleGroup.TRICEPS.name], exercise=[Exercise.SKULL_CRUSHERS.name]),
            WorkPlanScheduleDay(muscle_group=[MuscleGroup.BICEPS.name], exercise=[Exercise.PREACHER_CURL.name]),
            WorkPlanScheduleDay(muscle_group=[MuscleGroup.CALVES.name], exercise=[Exercise.STANDING_CALF_RAISE.name]),
        ],
        wednesday=[
            WorkPlanScheduleDay(muscle_group=[MuscleGroup.ABS.name], exercise=[Exercise.DECLINE_CRUNCH.name]),
            WorkPlanScheduleDay(muscle_group=[MuscleGroup.ABS.name], exercise=[Exercise.DRAGON_FLAG.name]),
            WorkPlanScheduleDay(muscle_group=[MuscleGroup.ABS.name], exercise=[Exercise.JACKKNIFE_SIT_UP.name]),
            WorkPlanScheduleDay(muscle_group=[MuscleGroup.FOREARMS.name], exercise=[Exercise.FARMERS_WALK.name]),
            WorkPlanScheduleDay(muscle_group=[MuscleGroup.FOREARMS.name], exercise=[Exercise.WRIST_CURL.name]),
            WorkPlanScheduleDay(muscle_group=[MuscleGroup.FOREARMS.name], exercise=[Exercise.REVERSE_WRIST_CURL.name]),
        ],
        thursday=[
            WorkPlanScheduleDay(muscle_group=[MuscleGroup.CHEST.name], exercise=[Exercise.INCLINE_BENCH_PRESS.name]),
            WorkPlanScheduleDay(muscle_group=[MuscleGroup.QUADS.name], exercise=[Exercise.FRONT_SQUAT.name]),
            WorkPlanScheduleDay(muscle_group=[MuscleGroup.SHOULDERS.name], exercise=[Exercise.ARNOLD_PRESS.name]),
            WorkPlanScheduleDay(muscle_group=[MuscleGroup.LATS.name], exercise=[Exercise.PULLOWVER.name]),
            WorkPlanScheduleDay(muscle_group=[MuscleGroup.TRICEPS.name], exercise=[Exercise.TRICEP_DIP.name]),
            WorkPlanScheduleDay(muscle_group=[MuscleGroup.BICEPS.name], exercise=[Exercise.HAMMER_CURL.name]),
            WorkPlanScheduleDay(muscle_group=[MuscleGroup.HAMSTRINGS.name], exercise=[Exercise.GLUTE_HAM_RAISE.name]),
        ],
        friday=[
            WorkPlanScheduleDay(muscle_group=[MuscleGroup.CHEST.name], exercise=[Exercise.PUSH_UPS.name]),
            WorkPlanScheduleDay(muscle_group=[MuscleGroup.HAMSTRINGS.name], exercise=[Exercise.GOOD_MORNINGS.name]),
            WorkPlanScheduleDay(muscle_group=[MuscleGroup.SHOULDERS.name], exercise=[Exercise.LATERAL_RAISE.name]),
            WorkPlanScheduleDay(muscle_group=[MuscleGroup.UPPER_BACK.name], exercise=[Exercise.BENT_OVER_ROW.name]),
            WorkPlanScheduleDay(muscle_group=[MuscleGroup.TRICEPS.name], exercise=[Exercise.TRICEP_PUSHDOWN.name]),
            WorkPlanScheduleDay(muscle_group=[MuscleGroup.BICEPS.name], exercise=[Exercise.DUMBBELL_CURL.name]),
            WorkPlanScheduleDay(muscle_group=[MuscleGroup.CALVES.name], exercise=[Exercise.CALF_RAISES.name]),
        ],
        saturday=[],
        sunday=[],
    )
)