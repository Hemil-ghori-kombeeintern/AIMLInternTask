from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from bson import ObjectId
from dotenv import load_dotenv
from model.student import Student
import os



load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")

client = MongoClient(MONGO_URL)
db = client["student_db"]
students_collection = db["students"]


app = FastAPI(
    title="Student CRUD API"
)


def student_response(student):

    return {
        "id": str(student["_id"]),
        "name": student["name"],
        "age": student["age"],
        "course": student["course"]
    }

@app.get("/")
def home():
    return {
        "message": "Welcome to Student CRUD API",
        "status": "Server is running successfully"
    }

@app.post("/students")
def create_student(student: Student):

    student_data = student.model_dump()
    result = students_collection.insert_one(student_data)

    return {
        "message": "Student created successfully",
        "id": str(result.inserted_id)
    }


@app.get("/students")
def get_students():

    students = students_collection.find()

    result = []

    for student in students:
        result.append(student_response(student))

    return result

@app.get("/students/search")
def search_students(q: str):

    students = students_collection.find({
        "name": {
            "$regex": q,
            "$options": "i"
        }
    })

    result = []

    for student in students:
        result.append(student_response(student))

    return result

@app.get("/students/{student_id}")
def get_student(student_id: str):

    try:
        student = students_collection.find_one({
            "_id": ObjectId(student_id)
        })

    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Invalid student ID"
        )

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student_response(student)


@app.put("/students/{student_id}")
def update_student(student_id: str,student: Student):
    print(student)

    try:
        result = students_collection.update_one(
            {
                "_id": ObjectId(student_id)
            },
            {
                "$set": student.model_dump()
            }
        )

    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Invalid student ID"
        )

    if result.matched_count == 0:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return {
        "message": "Student updated successfully",
        "result": student_response(students_collection.find_one({"_id": ObjectId(student_id)}))
    }


@app.delete("/students/{student_id}")
def delete_student(student_id: str):

    try:
        result = students_collection.delete_one({
            "_id": ObjectId(student_id)
        })

    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Invalid student ID"
        )

    if result.deleted_count == 0:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return {
        "message": "Student deleted successfully",
        "result": student_id
    }