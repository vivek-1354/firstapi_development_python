from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from app.schemas.post import Post, PostCreate
from app.db.session import get_db
from app.services import post_services as ps


router = APIRouter()


@router.get('/', response_model=List[Post])
def get_posts(db:Session  = Depends(get_db)):
    return ps.get_all_posts(db) 


@router.get('/{id}',response_model=Post)
def get_posts(id:int, db:Session  = Depends(get_db)):
    return ps.get_post_by_id(id, db)


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=Post)
def create_post(post :PostCreate, db:Session  = Depends(get_db)):
    return ps.create_post(post, db)


@router.delete("/{id}")
def delete_post(id:int, db:Session  = Depends(get_db)):
    return ps.delete_post(id, db)
        

@router.put("/{id}", response_model=Post)
def update_post(id : int, updated_post:PostCreate, db:Session  = Depends(get_db)):
    return ps.update_post(id, updated_post, db)
