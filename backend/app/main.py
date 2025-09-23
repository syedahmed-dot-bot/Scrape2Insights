from fastapi import FastAPI
from .api.routes.health import router as health_router
from .core.config import settings

app = FastAPI(title = "Scrape2Insights API", version = "0.1.0")
app.include_router(health_router, prefix="/health", tags=["health"])

@app.get("/")
def root():
    return {"message": "Scrape2Insights backend is running"}

