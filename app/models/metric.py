from pydantic import BaseModel, Field
from typing import Dict, List, Optional
from datetime import datetime

class MetricItem(BaseModel):
    name: str = Field(..., min_length=2, max_length=128)
    value: float
    metric_type: str = Field(default="gauge", pattern="^(counter|gauge|histogram)$")
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    tags: Dict[str, str] = Field(default_factory=dict)

class IngestBatchRequest(BaseModel):
    source_id: str
    metrics: List[MetricItem]

class IngestBatchResponse(BaseModel):
    accepted: int
    dropped: int
    status: str
