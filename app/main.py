from fastapi import FastAPI
from app.db.session import engine
from app.db.base import Base
from app.routes import post, user

Base.metadata.create_all(bind=engine) 

app = FastAPI()

app.include_router(post.router, prefix='/posts', tags=["Posts"])
app.include_router(user.router, prefix="/users", tags=["Users"])

    
