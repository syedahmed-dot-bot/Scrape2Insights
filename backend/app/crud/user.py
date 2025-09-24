from sqlalchemy.orm import Session 
from sqlalchemy import select
from ..models.user import User
from ..core.security import hash_password

def get_user_by_email(db: Session, email: str) -> None:
    return db.execute(select(User).where(User.email == email)).scalar_one_or_none()

def create_user(db: Session, email: str, password: str, role: str = "user") -> User:
    user = User(email = email, password_hash = hash_password(password), role = role)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

