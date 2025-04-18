from sqlalchemy.orm import declarative_base

Base = declarative_base()

# Import all your models here so they get registered with Base
from models.post import Post
