from fastapi import FastAPI
from db.session import engine
from db.base import Base
from routes import post

Base.metadata.create_all(bind=engine) 

app = FastAPI()

app.include_router(post.router, prefix='/posts', tags=["Posts"])

    
