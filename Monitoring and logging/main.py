
import logging
import time
from datetime import datetime, timezone
from threading import Lock

from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import Response
from prometheus_client import (
    Counter,
    Histogram,
    Gauge,
    generate_latest,
    CONTENT_TYPE_LATEST,
)


logging.basicConfig(
    level=logging.INFO,
    format=(
        "%(asctime)s | %(levelname)s | "
        "%(name)s | %(message)s"
    ),
)

logger = logging.getLogger("fastapi-monitoring")


app = FastAPI(
    title="FastAPI Logging and Monitoring",
    description="API with request logging and Prometheus metrics",
    version="1.0.0",
)


start_time = time.time()

stats_lock = Lock()

request_count = 0
error_count = 0
total_response_time = 0.0


REQUESTS = Counter(
    "api_requests_total",
    "Total number of HTTP requests",
    ["method", "endpoint", "status_code"],
)

ERRORS = Counter(
    "api_errors_total",
    "Total number of HTTP error responses",
)

REQUEST_DURATION = Histogram(
    "api_request_duration_seconds",
    "HTTP request processing duration in seconds",
    ["method", "endpoint"],
)

IN_PROGRESS = Gauge(
    "api_requests_in_progress",
    "Number of HTTP requests currently being processed",
)


@app.middleware("http")
async def monitoring_middleware(request: Request, call_next):
    global request_count, error_count, total_response_time

    start = time.perf_counter()

    method = request.method
    path = request.url.path

    IN_PROGRESS.inc()

    logger.info(
        "Request started | method=%s | path=%s",
        method,
        path,
    )

    status_code = 500

    try:
        response = await call_next(request)
        status_code = response.status_code
        return response

    except Exception:
        logger.exception(
            "Unhandled exception | method=%s | path=%s",
            method,
            path,
        )
        raise

    finally:
        duration = time.perf_counter() - start

        IN_PROGRESS.dec()

        # Update application statistics.
        with stats_lock:
            request_count += 1
            total_response_time += duration

            if status_code >= 400:
                error_count += 1

        # Update Prometheus metrics.
        REQUESTS.labels(
            method=method,
            endpoint=path,
            status_code=str(status_code),
        ).inc()

        REQUEST_DURATION.labels(
            method=method,
            endpoint=path,
        ).observe(duration)

        if status_code >= 400:
            ERRORS.inc()

        logger.info(
            "Request completed | method=%s | path=%s | "
            "status=%s | duration=%.4fs",
            method,
            path,
            status_code,
            duration,
        )

@app.get("/")
def home():
    logger.info("Home endpoint called")

    return {
        "message": "FastAPI monitoring system is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


@app.get("/hello/{name}")
def hello(name: str):
    logger.info("Hello endpoint called for name=%s", name)

    return {
        "message": f"Hello, {name}!"
    }

@app.get("/test-error")
def test_error():
    logger.warning("Intentional error test endpoint called")

    raise HTTPException(
        status_code=500,
        detail="This is a test error",
    )

@app.get("/monitoring")
def monitoring():
    with stats_lock:
        requests = request_count
        errors = error_count
        total_time = total_response_time

    average_response_time = (
        total_time / requests if requests else 0.0
    )

    uptime = time.time() - start_time

    return {
        "application": "FastAPI Monitoring System",
        "status": "running",
        "uptime_seconds": round(uptime, 2),
        "total_requests": requests,
        "total_errors": errors,
        "successful_requests": requests - errors,
        "average_response_time_seconds": round(
            average_response_time, 4
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


@app.get("/metrics", include_in_schema=False)
def metrics():
    return Response(
        content=generate_latest(),
        media_type=CONTENT_TYPE_LATEST,
    )