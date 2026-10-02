from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/api/v1/healthz")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_ingest_metrics_valid():
    payload = {
        "source_id": "sensor-alpha-01",
        "metrics": [
            {"name": "cpu_usage_pct", "value": 42.5, "metric_type": "gauge"}
        ]
    }
    response = client.post("/api/v1/metrics/ingest", json=payload)
    assert response.status_code == 200
    assert response.json()["accepted"] == 1
