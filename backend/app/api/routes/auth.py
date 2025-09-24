from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from jose import JWTError, jwt

from ...db.session import get_db
from ...crud.user import get_user_by_email, create_user
from ...core.security import verify_password
from ...core.jwt import create_access_token, ALGORITHM
from ...core.config import settings
from ...schemas.user import UserOut, UserCreate
from ...schemas.auth import Token, Login

router = APIRouter()
oauth2_schema = OAuth2PasswordBearer(tokenUrl="/auth/login")


def get_current_user(token: str = Depends(oauth2_schema), db: Session = Depends(get_db)) -> UserOut:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail = "Could not validate credentials",
        headers = {"WWW-Authentication": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[ALGORITHM])
        sub: str | None = payload.get("sub")
        if sub is None:
            raise credentials_exception
    
    except JWTError:
        raise credentials_exception
    user = get_user_by_email(db, sub)
    if not user or not user.is_active:
        raise credentials_exception
    return UserOut.model_validate(user)

@router.post("/signup", response_model = UserOut, status_code=201)
def signup(body: UserCreate, db: Session = Depends(get_db)):
    existing = get_user_by_email(db, body.email)
    if existing:
        raise HTTPException(status_code= 400, detail = "Email already registered")
    user = create_user(db, email=body.email, password=body.password)
    return UserOut.model_validate(user)

@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = get_user_by_email(db, form_data.username)
    if not user or not verify_password(form_data.password, user.password_hash):
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    token = create_access_token(subject=user.email)
    return Token(access_token=token)

@router.get("/me", response_model=UserOut)
def me(current_user: UserOut = Depends(get_current_user)):
    return current_user