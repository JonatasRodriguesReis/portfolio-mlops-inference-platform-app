from fastapi import APIRouter
from pydantic import BaseModel
from services.simple_model import SimpleRuleBasedModel
from core.metrics import REQUEST_COUNT, REQUEST_LATENCY

router = APIRouter()
model = SimpleRuleBasedModel()

class InferenceRequest(BaseModel):
    text: str

class InferenceResponse(BaseModel):
    result: str

@router.post("/predict", response_model=InferenceResponse)
def predict(request: InferenceRequest):

    REQUEST_COUNT.inc()
    with REQUEST_LATENCY.time():
        output = model.predict(request.text)
    return {"result": output}
