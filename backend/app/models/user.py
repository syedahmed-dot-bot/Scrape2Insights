from sqlalchemy import Column, Integer, String, Boolean, DateTime, func, UniqueConstraint
from ..db.base import Base

class User(Base):
    __tablename__ = "users"
    __table_args__ = (UniqueConstraint("email", name="uq_users_email"),)

    id = Column(Integer, primary_key = True, index = True)
    email = Column(String(255), nullable = False, unique = True, index= True)
    password_hash = Column(String(255), nullable = False)
    role = Column(String(50), nullable = False, default= "user")
    is_active = Column(Boolean, nullable = False, default = True)
    created_at = Column(DateTime(timezone = True), server_default = func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
