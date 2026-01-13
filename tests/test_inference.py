from fastapi.testclient import TestClient
from app.src.main import app

client = TestClient(app)

def test_predict():
    response = client.post(
        "/inference/predict",
        json={"text": "hello world"}
    )
    assert response.status_code == 200
    assert "result" in response.json()
