from pydantic import BaseModel
from datetime import datetime

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: int = 0
    
    class Config:
        from_attributes = True

# this is postcreate model with currently requires all the property of PostBase class so simply 
# inherit or extends

class PostCreate(PostBase):
    pass


# response  here we want to send id and created_at date as well we simply extent the PostBase class
# and add id and create_at to response model

class Post(PostBase):
    id:int
    created_at:datetime
    