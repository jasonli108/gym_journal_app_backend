import logging
from datetime import date, datetime
from typing import List, Dict, Optional
from uuid import UUID, uuid4

from fastapi.encoders import jsonable_encoder
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware  # Import CORSMiddleware
from tinydb import TinyDB, Query
from passlib.context import CryptContext
from fastapi import Request
from fastapi.responses import Response

logger=logging.getLogger()
logger.info("starting main")

from models import (
    WorkoutSession,
    WorkoutSessionIn,
    ExerciseOut,
    User,
    UserInDB,
    Token,
    UserCreate,
    WorkoutPlanBase,
    WorkoutPlanInDB,
    WorkoutSessionOut,
    ExerciseLogOut,
)
from enums import MuscleGroup, EquipmentType, MechanicsType, MyCustomGroup
from exercises.main import Exercise
from exercises.all_exercises import get_exercises_by_muscle_group

# --- App and DB Initialization ---
app = FastAPI()

# Add CORS middleware
origins = [
    "http://localhost:5173",  # Default Vite development server port
    "http://localhost:8000",  # If frontend is served from here (e.g. for testing or production)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --- Database setup ---
def get_db():
    db = TinyDB("db.json")
    try:
        yield db
    finally:
        db.close()


UserQuery = Query()

# --- Security and Authentication Setup ---
# Password Hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# OAuth2 Scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# --- Security Helper Functions ---
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str):
    """Hashes the password, truncating to 72 bytes for bcrypt compatibility."""
    return pwd_context.hash(password.encode("utf-8")[:72])


def get_user(db: TinyDB, username: str):
    users_table = db.table("users")
    user = users_table.get(UserQuery.username == username)
    if user:
        return UserInDB(**user)


@app.middleware("http")
async def log_requests(request: Request, call_next):
    body = await request.body()
    logger.info("REQUEST BODY:{}".format(body.decode()))

    response = await call_next(request)
    return response


async def get_current_user(token: str = Depends(oauth2_scheme), db: TinyDB = Depends(get_db)):
    # For a simple prototype, we'll just check if the token is a valid username.
    # In a real app, you would decode a JWT here.
    user = get_user(db, username=token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


# --- API Endpoints ---
@app.get("/")
async def read_root():
    return {"message": "Welcome to the Gym Journal API! Visit /docs for documentation."}


# --- Auth Endpoints ---
@app.post("/register/", response_model=User)
async def register_user(user_in: UserCreate, db: TinyDB = Depends(get_db)):
    users_table = db.table("users")
    if get_user(db, user_in.username):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Username already registered"
        )
    hashed_password = get_password_hash(user_in.password)
    user_db = UserInDB(username=user_in.username, hashed_password=hashed_password)
    users_table.insert(user_db.model_dump())
    return User(username=user_in.username)


@app.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(), db: TinyDB = Depends(get_db)
):
    user = get_user(db, form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # For simplicity, we'll use the username as the token. A real app should use JWT.
    access_token = user.username
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/users/me/", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user


@app.get("/users/me/workouts/", response_model=List[WorkoutSessionOut])
async def get_my_workouts(
    current_user: User = Depends(get_current_user),
    db: TinyDB = Depends(get_db),
    limit: Optional[int] = None,
):
    workouts_table = db.table("workouts")
    results = workouts_table.search(UserQuery.user_id == current_user.username)

    # Sort results by date
    results.sort(key=lambda x: datetime.fromisoformat(x['session_date']), reverse=True)

    # Apply limit
    if limit:
        results = results[:limit]

    sessions_out = []
    for res in results:
        exercise_logs_out = []
        for ex_log_data in res["exercises"]:
            exercise_logs_out.append(ExerciseLogOut(**ex_log_data))

        sessions_out.append(
            WorkoutSessionOut(
                session_id=res.get("session_id"),
                user_id=res["user_id"],
                session_date=res["session_date"],
                exercises=exercise_logs_out,
            )
        )
    return sessions_out


@app.post("/workoutplans/", response_model=WorkoutPlanInDB)
async def create_work_plan(
    work_plan_in: WorkoutPlanBase,
    current_user: User = Depends(get_current_user),
    db: TinyDB = Depends(get_db),
):
    logger.info("work_plan_in:{}".format(work_plan_in))
    logger.info("work_plan_schedule:{}".format(work_plan_in.workoutplan_schedule))
    if work_plan_in.user_id != current_user.username:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You can only create a workout plan for your own user.",
        )

    workoutplans_table = db.table("workoutplans")
    new_work_plan = WorkoutPlanInDB(
        user_id=work_plan_in.user_id,
        name=work_plan_in.name,
        workoutplan_summary=work_plan_in.workoutplan_summary,
        workoutplan_schedule=work_plan_in.workoutplan_schedule,
        workoutplan_id=uuid4() # Explicitly generate UUID
    )
    work_plan_data = new_work_plan.model_dump()
    work_plan_data["workoutplan_id"] = str(new_work_plan.workoutplan_id)
    # The `jsonable_encoder` was converting the Exercise enum to a dict, which the pydantic validator doesn't expect on the way back out.
    # We can manually convert the schedule to a json-friendly format, and the validator will handle it on the way back out.
    work_plan_data['workoutplan_schedule'] = jsonable_encoder(new_work_plan.workoutplan_schedule)

    logger.info("Inserting work_plan_data into TinyDB: {}".format(work_plan_data))
    workoutplans_table.insert(work_plan_data)
    return new_work_plan


@app.get("/users/{user_id}/workoutplans/", response_model=List[WorkoutPlanInDB])
async def get_user_work_plans(
    user_id: str, current_user: User = Depends(get_current_user), db: TinyDB = Depends(get_db)
):

    if user_id == "me":
        user_id = current_user.username
    elif user_id != current_user.username:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You can only view your own workout plans.",
        )
    workoutplans_table = db.table("workoutplans")
    user_workoutplans = workoutplans_table.search(UserQuery.user_id == user_id)
    for wp in user_workoutplans:
        logger.info("Raw workout plan from TinyDB (get_user_work_plans): {}".format(wp))
        if "name" not in wp or wp["name"] is None:
            wp["name"] = wp["workoutplan_summary"]["goal"]
        # Handle renaming 'id' to 'workoutplanScheduleId' for backward compatibility
        if (
            "workoutplan_schedule" in wp
            and wp["workoutplan_schedule"] is not None
            and "id" in wp["workoutplan_schedule"]
        ):
            wp["workoutplan_schedule"]["workoutplanScheduleId"] = wp["workoutplan_schedule"].pop("id")
    return [WorkoutPlanInDB(**wp) for wp in user_workoutplans]


@app.get("/users/me/workoutplans/latest/", response_model=List[WorkoutPlanInDB])
async def get_my_latest_workout_plans(
    current_user: User = Depends(get_current_user),
    db: TinyDB = Depends(get_db),
    limit: Optional[int] = None,
):
    workoutplans_table = db.table("workoutplans")
    results = workoutplans_table.search(UserQuery.user_id == current_user.username)

    # Since TinyDB does not provide automatic timestamps,
    # and workoutplan_id is a UUID (which contains a timestamp),
    # we can sort by the UUID string. This gives a rough chronological order.
    # For precise ordering, a 'created_at' field should be added to the model.
    results.sort(key=lambda x: x['workoutplan_id'], reverse=True)

    # Apply limit
    if limit:
        results = results[:limit]

    for wp in results:
        logger.info("Raw workout plan from TinyDB (get_my_latest_workout_plans): {}".format(wp))
        # Handle renaming 'id' to 'workoutplanScheduleId' for backward compatibility
        if (
            "workoutplan_schedule" in wp
            and wp["workoutplan_schedule"] is not None
            and "id" in wp["workoutplan_schedule"]
        ):
            wp["workoutplan_schedule"]["workoutplanScheduleId"] = wp["workoutplan_schedule"].pop("id")

    return [WorkoutPlanInDB(**wp) for wp in results]


@app.get("/workoutplans/{workoutplan_id}", response_model=WorkoutPlanInDB)
async def get_work_plan_by_id(
    workoutplan_id: UUID,
    current_user: User = Depends(get_current_user),
    db: TinyDB = Depends(get_db),
):
    workoutplans_table = db.table("workoutplans")
    workoutplan_query = Query()
    work_plan = workoutplans_table.get(workoutplan_query.workoutplan_id == str(workoutplan_id))

    logger.info("Raw workout plan from TinyDB (get_work_plan_by_id): {}".format(work_plan))

    if not work_plan:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Work plan not found"
        )
    if work_plan["user_id"] != current_user.username:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You are not authorized to access this work plan.",
        )
    # Handle renaming 'id' to 'workoutplanScheduleId' for backward compatibility
    if (
        "workoutplan_schedule" in work_plan
        and work_plan["workoutplan_schedule"] is not None
        and "id" in work_plan["workoutplan_schedule"]
    ):
        work_plan["workoutplan_schedule"]["workoutplanScheduleId"] = work_plan["workoutplan_schedule"].pop("id")
    return WorkoutPlanInDB(**work_plan)


@app.put("/workoutplans/{workoutplan_id}", response_model=WorkoutPlanInDB)
async def update_work_plan(
    workoutplan_id: UUID,
    work_plan_in: WorkoutPlanBase,
    current_user: User = Depends(get_current_user),
    db: TinyDB = Depends(get_db),
):
    workoutplans_table = db.table("workoutplans")
    workoutplan_query = Query()

    # Check if the work plan exists
    existing_workoutplan = workoutplans_table.get(workoutplan_query.workoutplan_id == str(workoutplan_id))

    if work_plan_in.user_id != current_user.username:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You can only create/update a workout plan for your own user."
        )

    if existing_workoutplan:
        # Update existing work plan
        if existing_workoutplan["user_id"] != current_user.username:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You are not authorized to update this work plan."
            )
        
        updated_work_plan = WorkoutPlanInDB(
            user_id=work_plan_in.user_id,
            name=work_plan_in.name,
            workoutplan_summary=work_plan_in.workoutplan_summary,
            workoutplan_schedule=work_plan_in.workoutplan_schedule,
            workoutplan_id=workoutplan_id
        )
        work_plan_data = updated_work_plan.model_dump()
        work_plan_data["workoutplan_id"] = str(updated_work_plan.workoutplan_id)
        work_plan_data['workoutplan_schedule'] = jsonable_encoder(updated_work_plan.workoutplan_schedule)
        logger.info("Updating work_plan_data in TinyDB: {}".format(work_plan_data))
        workoutplans_table.update(work_plan_data, workoutplan_query.workoutplan_id == str(workoutplan_id))
        return updated_work_plan
    else:
        # Create new work plan if not found
        new_work_plan = WorkoutPlanInDB(
            user_id=work_plan_in.user_id,
            name=work_plan_in.name,
            workoutplan_summary=work_plan_in.workoutplan_summary,
            workoutplan_schedule=work_plan_in.workoutplan_schedule,
            workoutplan_id=workoutplan_id
        )
        work_plan_data = new_work_plan.model_dump()
        work_plan_data["workoutplan_id"] = str(new_work_plan.workoutplan_id)
        work_plan_data['workoutplan_schedule'] = jsonable_encoder(new_work_plan.workoutplan_schedule)
        
        workoutplans_table.insert(work_plan_data)
        # Using status.HTTP_201_CREATED for creation, but FastAPI's @app.put
        # defaults to 200/204. If 201 is strictly needed for creation,
        # a separate POST endpoint or a custom response would be better.
        # For now, we return 200 OK as PUT is idempotent and can create.
        return new_work_plan




@app.delete("/workoutplans/{workoutplan_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_work_plan(
    workoutplan_id: UUID,
    current_user: User = Depends(get_current_user),
    db: TinyDB = Depends(get_db),
):
    workoutplans_table = db.table("workoutplans")
    workoutplan_query = Query()

    # Check if the work plan exists and belongs to the current user
    existing_workoutplan = workoutplans_table.get(workoutplan_query.workoutplan_id == str(workoutplan_id))

    if not existing_workoutplan:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Work plan not found"
        )
    if existing_workoutplan["user_id"] != current_user.username:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You are not authorized to delete this work plan.",
        )
    
    workoutplans_table.remove(workoutplan_query.workoutplan_id == str(workoutplan_id))
    return {"message": "Workout plan deleted successfully"}
@app.post("/workouts/", response_model=WorkoutSessionOut)
async def create_workout_session(session_in: WorkoutSessionIn, db: TinyDB = Depends(get_db)):
    logger.info("Received workout session data: {}".format(session_in.model_dump()))
    logger.debug("Received workout session data: {}".format(session_in.model_dump()))
    workouts_table = db.table("workouts")
    new_session = WorkoutSession(**session_in.model_dump())
    session_data = new_session.model_dump(exclude={"session_id"})
    session_data["session_date"] = session_data["session_date"].isoformat()

    exercises_to_insert = []
    for ex_log in new_session.exercises:
        exercises_to_insert.append(
            {
                "exercise": ex_log.exercise.value.display_name,
                "sets": ex_log.sets,
                "reps": ex_log.reps,
                "weight": jsonable_encoder(ex_log.weight),
            }
        )
    session_data["exercises"] = exercises_to_insert

    workouts_table.insert(session_data | {"session_id": str(new_session.session_id)})

    exercise_logs_out = []
    for ex_log in new_session.exercises:
        exercise_logs_out.append(
            ExerciseLogOut(
                exercise=ex_log.exercise.value.display_name,
                sets=ex_log.sets,
                reps=ex_log.reps,
                weight=ex_log.weight,
            )
        )
    logger.info("exercise_logs_out:{}".format(exercise_logs_out))
    logger.debug("exercise_logs_out:{}".format(exercise_logs_out))
    return WorkoutSessionOut(
        session_id=new_session.session_id,
        user_id=new_session.user_id,
        session_date=new_session.session_date,
        exercises=exercise_logs_out,
    )


@app.delete("/workouts/{session_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_workout_session(
    session_id: UUID,
    current_user: User = Depends(get_current_user),
    db: TinyDB = Depends(get_db),
):
    workouts_table = db.table("workouts")
    workout_query = Query()

    existing_session = workouts_table.get(workout_query.session_id == str(session_id))

    if not existing_session:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Workout session not found"
        )
    if existing_session["user_id"] != current_user.username:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You are not authorized to delete this workout session.",
        )
    
    workouts_table.remove(workout_query.session_id == str(session_id))
    return {"message": "Workout session deleted successfully"}


@app.put("/workouts/{session_id}", response_model=WorkoutSessionOut)
async def update_workout_session(
    session_id: UUID,
    session_in: WorkoutSessionIn,
    current_user: User = Depends(get_current_user),
    db: TinyDB = Depends(get_db),
):
    workouts_table = db.table("workouts")
    workout_query = Query()

    existing_session = workouts_table.get(workout_query.session_id == str(session_id))

    if not existing_session:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Workout session not found"
        )
    if existing_session["user_id"] != current_user.username:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You are not authorized to update this workout session.",
        )
    
    # Update the session
    updated_session = WorkoutSession(**session_in.model_dump(), session_id=session_id)
    session_data = updated_session.model_dump(exclude={"session_id"})
    session_data["session_date"] = session_data["session_date"].isoformat()

    exercises_to_insert = []
    for ex_log in updated_session.exercises:
        exercises_to_insert.append(
            {
                "exercise": ex_log.exercise.value.display_name,
                "sets": ex_log.sets,
                "reps": ex_log.reps,
                "weight": jsonable_encoder(ex_log.weight),
            }
        )
    session_data["exercises"] = exercises_to_insert

    workouts_table.update(session_data | {"session_id": str(updated_session.session_id)}, workout_query.session_id == str(session_id))

    exercise_logs_out = []
    for ex_log in updated_session.exercises:
        exercise_logs_out.append(
            ExerciseLogOut(
                exercise=ex_log.exercise.value.display_name,
                sets=ex_log.sets,
                reps=ex_log.reps,
                weight=ex_log.weight,
            )
        )
    
    return WorkoutSessionOut(
        session_id=updated_session.session_id,
        user_id=updated_session.user_id,
        session_date=updated_session.session_date,
        exercises=exercise_logs_out,
    )


@app.get("/users/{user_id}/workouts/", response_model=List[WorkoutSessionOut])
async def get_user_workouts(
    user_id: str, db: TinyDB = Depends(get_db), session_date: Optional[date] = None
):
    workouts_table = db.table("workouts")
    query = UserQuery.user_id == user_id
    if session_date:
        query = query & (UserQuery.session_date == str(session_date))
    results = workouts_table.search(query)

    sessions_out = []
    for res in results:
        exercise_logs_out = []
        for ex_log_data in res["exercises"]:
            exercise_logs_out.append(ExerciseLogOut(**ex_log_data))

        sessions_out.append(
            WorkoutSessionOut(
                session_id=res.get("session_id"),
                user_id=res["user_id"],
                session_date=res["session_date"],
                exercises=exercise_logs_out,
            )
        )
    return sessions_out


# --- Exercise Endpoints ---
@app.get("/exercises/", response_model=List[ExerciseOut])
async def get_exercises(
    muscle_group: Optional[MuscleGroup] = None,
    equipment_type: Optional[EquipmentType] = None,
    mechanics_type: Optional[MechanicsType] = None,
    my_custom_group: Optional[MyCustomGroup] = None,
    is_popular: Optional[bool] = None,
):
    logger.info("get exercises starting")
    all_exercises = []
    if muscle_group:
        exercises_to_filter = get_exercises_by_muscle_group(muscle_group).values()
    else:
        exercises_to_filter = [member.value for member in Exercise]

    for exercise_def in exercises_to_filter:
        if (
            (equipment_type and exercise_def.equipment_type != equipment_type)
            or (mechanics_type and exercise_def.mechanics_type != mechanics_type)
            or (my_custom_group and exercise_def.my_custom_group != my_custom_group)
            or (is_popular is not None and exercise_def.is_popular != is_popular)
        ):
            continue
        exercise_data = ExerciseOut(
            id=exercise_def.id,
            display_name=exercise_def.display_name,
            muscle_group=exercise_def.muscle_group,
            url=exercise_def.url,
            is_popular=exercise_def.is_popular,
            equipment_type=exercise_def.equipment_type,
            mechanics_type=exercise_def.mechanics_type,
            my_custom_group=exercise_def.my_custom_group,
        )
        all_exercises.append(exercise_data)
    return all_exercises
