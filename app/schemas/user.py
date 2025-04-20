from pydantic import BaseModel
from datetime import datetime

class UserBase(BaseModel):
    username: str
    email: str
    password: str
    
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
    

class LoginRequest(BaseModel):
    email:str
    password:str
    
class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

    