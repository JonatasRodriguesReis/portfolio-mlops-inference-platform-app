from fastapi import FastAPI
from api.inference import router as inference_router
from api.health import router as health_router
from api.metrics import router as metrics_router

app = FastAPI(
    title="MLOps Inference Platform App",
    version="0.1.0"
)

app.include_router(inference_router, prefix="/inference")
app.include_router(health_router)
app.include_router(metrics_router)
