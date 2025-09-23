from fastapi import APIRouter

router = APIRouter()

@router.get("/", summary = "Health Check")
def health():
    return {"service": "scrape2insights-api", "status": "ok"}

