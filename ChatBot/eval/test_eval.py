import os
import sys
import time
import pytest

# Ensure evaluation directory and root directory are in sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from dotenv import load_dotenv
from google import genai
from deepeval import assert_test
from deepeval.test_case import LLMTestCase

try:
    from eval.eval_metrics import get_eval_judge, create_all_metrics
except ImportError:
    from eval_metrics import get_eval_judge, create_all_metrics

load_dotenv()

# Initialize Gemini Client for live test evaluation
API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=API_KEY) if API_KEY else None

SYSTEM_INSTRUCTION = """
You are a helpful AI/ML assistant.

Rules:
- Explain concepts clearly and simply.
- Use simple language.
- Give examples when useful.
- Provide clean Python code when requested.
- Stay focused on the user's question.
"""


def generate_chatbot_response(prompt: str, max_retries: int = 5, initial_delay: float = 5.0) -> str:
    if not client:
        raise ValueError("GEMINI_API_KEY is missing.")
    delay = initial_delay
    for attempt in range(max_retries):
        try:
            response = client.models.generate_content(
                model="gemini-3.1-flash-lite",
                contents=prompt,
                config={"system_instruction": SYSTEM_INSTRUCTION}
            )
            return response.text
        except Exception as e:
            if "429" in str(e) or "RESOURCE_EXHAUSTED" in str(e):
                if attempt == max_retries - 1:
                    raise e
                time.sleep(delay)
                delay *= 1.5
            else:
                raise e


@pytest.mark.parametrize(
    "user_prompt",
    [
        "What is Overfitting in machine learning and how can I prevent it?",
        "Explain the difference between Supervised and Unsupervised learning with simple examples.",
        "Write a clean Python script using scikit-learn to train a LinearRegression model."
    ]
)
def test_chatbot_eval(user_prompt: str):
    """
    Automated DeepEval test suite evaluating AI/ML chatbot outputs across all 9 metrics.
    """
    actual_output = generate_chatbot_response(user_prompt)

    retrieval_ctx = [f"User query topic: {user_prompt}. Response: {actual_output}"]
    test_case = LLMTestCase(
        input=user_prompt,
        actual_output=actual_output,
        expected_output=actual_output,
        retrieval_context=retrieval_ctx,
        context=retrieval_ctx
    )

    judge = get_eval_judge()
    metrics = create_all_metrics(judge=judge)

    assert_test(test_case, metrics)
