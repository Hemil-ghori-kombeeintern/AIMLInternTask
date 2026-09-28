import sqlite3
import os
import uuid
from datetime import datetime, timezone

from dotenv import load_dotenv
from google import genai
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

load_dotenv()

DB_NAME = "feedback.db"

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError(
        "GEMINI_API_KEY not found. Add it to your .env file."
    )

client = genai.Client(api_key=api_key)

app = FastAPI(title="AI Feedback Loop API")


def get_connection():
    return sqlite3.connect(DB_NAME)


def initialize_database():
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS responses (
                response_id TEXT PRIMARY KEY,
                question TEXT NOT NULL,
                answer TEXT NOT NULL,
                created_at TEXT NOT NULL
            )
        """)

        conn.execute("""
            CREATE TABLE IF NOT EXISTS feedback (
                feedback_id INTEGER PRIMARY KEY AUTOINCREMENT,
                response_id TEXT NOT NULL,
                rating INTEGER NOT NULL CHECK (rating IN (1, -1)),
                comment TEXT,
                created_at TEXT NOT NULL,
                FOREIGN KEY(response_id)
                    REFERENCES responses(response_id)
            )
        """)


initialize_database()


class QuestionRequest(BaseModel):
    question: str = Field(
        min_length=1,
        max_length=2000
    )


class FeedbackRequest(BaseModel):
    response_id: str
    rating: int = Field(
        description="1 for positive, -1 for negative"
    )
    comment: str | None = Field(
        default=None,
        max_length=2000
    )


def generate_answer(question: str) -> str:
    prompt = (
        f"{question}\n\n"
        "Give a paragraph of approximately 150 to 250 words. "
        "Do not stop after the introduction."
    )

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=prompt,
        config={
            "max_output_tokens": 200,
            "temperature": 0.1,
            "thinking_config": {
                "thinking_level": "minimal"
            }
        }
    )

    generated_text = (response.text or "").strip()

    if not generated_text:
        return "No text was returned."

    return generated_text


@app.post("/ask")
def ask_question(request: QuestionRequest):
    response_id = str(uuid.uuid4())

    answer = generate_answer(request.question)
    created_at = datetime.now(timezone.utc).isoformat()

    with get_connection() as conn:
        conn.execute(
            """
            INSERT INTO responses (
                response_id,
                question,
                answer,
                created_at
            )
            VALUES (?, ?, ?, ?)
            """,
            (
                response_id,
                request.question,
                answer,
                created_at
            )
        )

    return {
        "response_id": response_id,
        "question": request.question,
        "answer": answer,
        "message": "Please provide feedback using response_id."
    }


@app.post("/feedback")
def submit_feedback(request: FeedbackRequest):

    if request.rating not in (1, -1):
        raise HTTPException(
            status_code=400,
            detail="Rating must be 1 or -1."
        )

    with get_connection() as conn:

        existing_response = conn.execute(
            """
            SELECT response_id
            FROM responses
            WHERE response_id = ?
            """,
            (request.response_id,)
        ).fetchone()

        if existing_response is None:
            raise HTTPException(
                status_code=404,
                detail="Response ID not found."
            )

        conn.execute(
            """
            INSERT INTO feedback (
                response_id,
                rating,
                comment,
                created_at
            )
            VALUES (?, ?, ?, ?)
            """,
            (
                request.response_id,
                request.rating,
                request.comment,
                datetime.now(timezone.utc).isoformat()
            )
        )

    return {
        "message": "Feedback stored successfully.",
        "response_id": request.response_id,
        "rating": request.rating
    }


@app.get("/feedback")
def get_feedback():

    with get_connection() as conn:
        conn.row_factory = sqlite3.Row

        rows = conn.execute(
            """
            SELECT
                r.response_id,
                r.question,
                r.answer,
                f.rating,
                f.comment,
                f.created_at AS feedback_time
            FROM feedback f
            JOIN responses r
                ON r.response_id = f.response_id
            ORDER BY f.feedback_id DESC
            """
        ).fetchall()

    return [dict(row) for row in rows]


@app.get("/feedback/summary")
def feedback_summary():

    with get_connection() as conn:
        row = conn.execute(
            """
            SELECT
                COUNT(*) AS total_feedback,

                SUM(
                    CASE
                        WHEN rating = 1 THEN 1
                        ELSE 0
                    END
                ) AS positive_feedback,

                SUM(
                    CASE
                        WHEN rating = -1 THEN 1
                        ELSE 0
                    END
                ) AS negative_feedback

            FROM feedback
            """
        ).fetchone()

    total = row[0] or 0
    positive = row[1] or 0
    negative = row[2] or 0

    positive_rate = (
        round((positive / total) * 100, 2)
        if total > 0
        else 0
    )

    return {
        "total_feedback": total,
        "positive_feedback": positive,
        "negative_feedback": negative,
        "positive_feedback_percentage": positive_rate
    }


@app.get("/health")
def health():
    return {"status": "healthy"}
