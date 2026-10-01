from fastapi import FastAPI
from app.api.endpoints import router as api_router
from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
    description="High-throughput telemetry ingestion router"
)

app.include_router(api_router, prefix="/api/v1")
