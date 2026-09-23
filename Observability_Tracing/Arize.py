import os

from google import genai
from dotenv import load_dotenv

load_dotenv()

from openinference.instrumentation.google_genai import (
    GoogleGenAIInstrumentor,
)

from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import (
    OTLPSpanExporter,
)

tracer_provider = TracerProvider()

exporter = OTLPSpanExporter(
    endpoint="http://127.0.0.1:4317",
    insecure=True,
)

tracer_provider.add_span_processor(
    SimpleSpanProcessor(exporter)
)

GoogleGenAIInstrumentor().instrument(
    tracer_provider=tracer_provider
)

client = genai.Client(
    api_key=os.environ["GEMINI_API_KEY"]
)

response = client.models.generate_content(
    model="gemini-3.1-flash-lite",
    contents="Explain AI observability in simple words."
)

print("Gemini response:")
print(response.text)