from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from app.schemas.user import User, UserCreate, LoginRequest, TokenResponse
from app.db.session import get_db
from app.services import post_services as ps
from app.services import user_service as us


router = APIRouter()


@router.post("/login", response_model=TokenResponse)
def login(user: LoginRequest, db: Session = Depends(get_db)):
    return us.user_login(user, db)


@router.get('/', response_model=List[User])
def get_users(db:Session  = Depends(get_db)):
    return us.get_all_users(db) 


@router.get('/{id}',response_model=User)
def get_user(id:int, db:Session  = Depends(get_db)):
    return us.get_user_by_id(id, db)


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=User)
def create_user(post :UserCreate, db:Session  = Depends(get_db)):
    return us.create_user(post, db)


@router.delete("/{id}")
def delete_user(id:int, db:Session  = Depends(get_db)):
    return us.delete_user(id, db)
        

# @router.put("/{id}", response_model=Post)
# def update_post(id : int, updated_post:PostCreate, db:Session  = Depends(get_db)):
#     return ps.update_post(id, updated_post, db)
