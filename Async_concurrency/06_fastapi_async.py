from fastapi import FastAPI
import asyncio

app = FastAPI(
    title="Async FastAPI Demo"
)


@app.get("/")
async def home():

    return {
        "message": "FastAPI Async API"
    }


@app.get("/data")
async def get_data():

    print("Processing request...")

    await asyncio.sleep(3)

    return {
        "message": "Data received"
    }


@app.get("/users/{user_id}")
async def get_user(user_id: int):

    await asyncio.sleep(1)

    return {
        "user_id": user_id,
        "name": "Demo User"
    }