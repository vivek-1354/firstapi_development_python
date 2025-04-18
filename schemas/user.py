from pydantic import BaseModel
from datetime import datetime

class UserBase(BaseModel):
    username: str
    email: str
    password: int
    
    class Config:
        from_attributes = True


class UserCreate(UserBase):
    pass


# response
class User(BaseModel):
    id:int
    username: str
    email: str
    created_at:datetime
    

class UserLogin(BaseModel):
    email:str
    password:int
    