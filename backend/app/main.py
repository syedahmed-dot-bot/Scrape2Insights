from fastapi import FastAPI
from .api.routes.health import router as health_router
from .core.config import settings
from .api.routes.auth import router as auth_router

app = FastAPI(title = settings.APP_NAME, version = "0.1.0")
app.include_router(health_router, prefix="/health", tags=["health"])
app.include_router(auth_router, prefix="/auth", tags = ["auth"])

@app.get("/")
def root():
    return {"message": "Scrape2Insights backend is running", "env": settings.ENV}

