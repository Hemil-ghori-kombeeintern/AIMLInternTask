from fastapi import FastAPI
from pydantic import BaseModel

from model import predict_result


app = FastAPI(
    title="Dockerized ML API",
    description="Simple ML API running inside Docker",
    version="1.0"
)


class Student(BaseModel):
    study_hours: float
    attendance: float


@app.get("/")
def home():

    return {
        "message": "Dockerized ML API is running!"
    }


@app.get("/health")
def health():

    return {
        "status": "healthy"
    }


@app.post("/predict")
def predict(student: Student):

    result = predict_result(
        student.study_hours,
        student.attendance
    )

    return {
        "study_hours": student.study_hours,
        "attendance": student.attendance,
        "prediction": result
    }