from sqlalchemy import TIMESTAMP, Boolean, Column, Integer, String, text
from app.db.base import Base

class Post(Base):
    __tablename__ = 'posts'
    
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String,nullable=False)
    content = Column(String, nullable=False)
    rating = Column(Integer, nullable=True, default=0)
    published = Column(Boolean, server_default="TRUE")
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))