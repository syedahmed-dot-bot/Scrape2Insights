from fastapi import Depends, APIRouter
from .auth import require_role
from ...schemas.user import UserOut

router = APIRouter()

@router.get("/ping")
def admin_ping(_: UserOut = Depends(require_role("admin"))):
    return {"ok": True, "scope": "admin"}