from sqlalchemy.orm import declarative_base

Base = declarative_base()

# Import all your models here so they get registered with Base
from app.models.post import Post
from app.models.user import User
