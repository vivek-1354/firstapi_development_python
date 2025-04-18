from sqlalchemy import TIMESTAMP, Column, Integer, String, text
from db.base import Base

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String,nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(Integer, nullable=True, default=0)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))