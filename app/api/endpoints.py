from fastapi import APIRouter, HTTPException, status
from app.models.metric import IngestBatchRequest, IngestBatchResponse

router = APIRouter()

@router.get("/healthz", status_code=status.HTTP_200_OK)
async def health_check():
    return {"status": "healthy", "service": "cloud-telemetry-service"}

@router.post("/metrics/ingest", response_model=IngestBatchResponse)
async def ingest_metrics(payload: IngestBatchRequest):
    if not payload.metrics:
        raise HTTPException(status_code=400, detail="Empty metric batch rejected")
    
    return IngestBatchResponse(
        accepted=len(payload.metrics),
        dropped=0,
        status="buffered"
    )
