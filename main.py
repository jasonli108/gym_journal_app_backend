import sqlalchemy
from fastapi import FastAPI
from pydantic import BaseModel
from databases import Database
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

# Database setup
DATABASE_URL = "sqlite:///./gym_journal.db"
database = Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

workouts = sqlalchemy.Table(
    "workouts",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("exercise", sqlalchemy.String),
    sqlalchemy.Column("reps", sqlalchemy.Integer),
    sqlalchemy.Column("weight", sqlalchemy.Float),
    sqlalchemy.Column("date", sqlalchemy.String, default=datetime.utcnow),
)

engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
metadata.create_all(engine)


# Pydantic models
class WorkoutIn(BaseModel):
    exercise: str
    reps: int
    weight: float


class Workout(BaseModel):
    id: int
    exercise: str
    reps: int
    weight: float
    date: str


app = FastAPI()

# CORS middleware
origins = [
    "http://localhost:3000",
    "http://localhost:5173", # for vite
    "http://127.0.0.1:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/workouts/", response_model=list[Workout])
async def read_workouts():
    query = workouts.select()
    return await database.fetch_all(query)


@app.post("/workouts/", response_model=Workout)
async def create_workout(workout: WorkoutIn):
    query = workouts.insert().values(exercise=workout.exercise, reps=workout.reps, weight=workout.weight, date=datetime.utcnow().isoformat())
    last_record_id = await database.execute(query)
    return {**workout.dict(), "id": last_record_id, "date": datetime.utcnow().isoformat()}


@app.get("/workouts/{workout_id}", response_model=Workout)
async def read_workout(workout_id: int):
    query = workouts.select().where(workouts.c.id == workout_id)
    return await database.fetch_one(query)


@app.put("/workouts/{workout_id}", response_model=Workout)
async def update_workout(workout_id: int, workout: WorkoutIn):
    query = (
        workouts.update()
        .where(workouts.c.id == workout_id)
        .values(exercise=workout.exercise, reps=workout.reps, weight=workout.weight)
    )
    await database.execute(query)
    return {**workout.dict(), "id": workout_id, "date": datetime.utcnow().isoformat()}


@app.delete("/workouts/{workout_id}")
async def delete_workout(workout_id: int):
    query = workouts.delete().where(workouts.c.id == workout_id)
    await database.execute(query)
    return {"message": "Workout deleted successfully"}
