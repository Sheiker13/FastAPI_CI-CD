from fastapi import FastAPI
from .logger import logger
from .metrics import REQUEST_COUNT, REQUEST_LATENCY
from fastapi import Response
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
import time

app = FastAPI()

@app.get("/")
def read_root():
    start_time = time.time()
    REQUEST_COUNT.labels(method='GET', endpoint='/').inc()
    response = {"message": "Hello, CI/CD World!"}
    latency = time.time() - start_time
    REQUEST_LATENCY.labels(endpoint='/').observe(latency)
    logger.info("Root endpoint accessed.")
    return response

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/metrics")
def metrics():
    data = generate_latest()
    return Response(content=data, media_type=CONTENT_TYPE_LATEST)