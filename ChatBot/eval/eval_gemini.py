import os
import time
from collections import deque
from threading import Lock
from typing import Optional, Type, Union
from pydantic import BaseModel
from google import genai
from google.genai.errors import APIError
from deepeval.models import DeepEvalBaseLLM
from dotenv import load_dotenv

load_dotenv()


class RPMLimiter:
    """
    Thread-safe Rate Limiter to strictly enforce a client-side limit of N requests per minute (RPM).
    Default max_rpm = 10 (Strictly max 10 requests per 60-second window).
    """

    def __init__(self, max_rpm: int = 10):
        self.max_rpm = max_rpm
        self.timestamps = deque()
        self.lock = Lock()

    def wait_if_needed(self):
        with self.lock:
            now = time.time()
            # Remove timestamps older than 60 seconds
            while self.timestamps and self.timestamps[0] <= now - 60:
                self.timestamps.popleft()

            # If max_rpm requests reached in 60s, wait until the oldest request expires
            if len(self.timestamps) >= self.max_rpm:
                oldest = self.timestamps[0]
                sleep_time = 60.0 - (now - oldest) + 0.1
                if sleep_time > 0:
                    time.sleep(sleep_time)
                now = time.time()
                while self.timestamps and self.timestamps[0] <= now - 60:
                    self.timestamps.popleft()

            self.timestamps.append(now)


# Global rate limiter set strictly to 10 RPM
global_rpm_limiter = RPMLimiter(max_rpm=10)


class GeminiLLM(DeepEvalBaseLLM):
    """
    Custom DeepEval LLM wrapper for Google Gemini models using google-genai SDK.
    Includes client-side 10 RPM rate-limiting and automatic 429 retry logic.
    """

    def __init__(self, model_name: str = "gemini-3.1-flash-lite", api_key: Optional[str] = None):
        self.model_name = model_name
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY environment variable is missing.")
        self.client = genai.Client(api_key=self.api_key)

    def load_model(self):
        return self.client

    def _call_with_retry(self, func, max_retries: int = 5, initial_delay: float = 5.0):
        """Executes API calls with 10 RPM throttling and exponential backoff retries."""
        delay = initial_delay
        for attempt in range(max_retries):
            try:
                # Enforce strict 10 RPM before firing request
                global_rpm_limiter.wait_if_needed()
                return func()
            except APIError as e:
                if e.code == 429 or "429" in str(e) or "RESOURCE_EXHAUSTED" in str(e):
                    if attempt == max_retries - 1:
                        raise e
                    time.sleep(delay)
                    delay *= 1.5
                else:
                    raise e
            except Exception as e:
                if "429" in str(e) or "RESOURCE_EXHAUSTED" in str(e):
                    if attempt == max_retries - 1:
                        raise e
                    time.sleep(delay)
                    delay *= 1.5
                else:
                    raise e

    def generate(self, prompt: str, schema: Optional[Type[BaseModel]] = None) -> Union[str, BaseModel]:
        """
        Synchronous text generation for DeepEval metric evaluations.
        Supports structured JSON output when a Pydantic schema is passed by DeepEval.
        """
        client = self.load_model()

        def _execute():
            if schema:
                response = client.models.generate_content(
                    model=self.model_name,
                    contents=prompt,
                    config={
                        "response_mime_type": "application/json",
                        "response_schema": schema,
                    }
                )
                return schema.model_validate_json(response.text)
            else:
                response = client.models.generate_content(
                    model=self.model_name,
                    contents=prompt
                )
                return response.text.strip()

        try:
            return self._call_with_retry(_execute)
        except Exception as e:
            if schema:
                prompt_with_instructions = (
                    f"{prompt}\n\nReturn ONLY a valid JSON matching this schema: {schema.model_json_schema()}"
                )

                def _fallback():
                    resp = client.models.generate_content(
                        model=self.model_name,
                        contents=prompt_with_instructions
                    )
                    return schema.model_validate_json(resp.text)

                return self._call_with_retry(_fallback)
            raise e

    async def a_generate(self, prompt: str, schema: Optional[Type[BaseModel]] = None) -> Union[str, BaseModel]:
        """
        Asynchronous generation method required by DeepEval.
        """
        return self.generate(prompt=prompt, schema=schema)

    def get_model_name(self) -> str:
        return f"Google Gemini ({self.model_name})"
