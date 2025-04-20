from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models.user import User
from app.utils.security import verify_password, create_access_token, hash_password

def get_all_users(db:Session):
    return db.query(User).all()

def user_login(request, db):
    user = db.query(User).filter(User.email == request.email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User with email not found")
    if not verify_password(request.password, user.password):
        raise HTTPException(status_code=400, detail="Incorrect password")
    token = create_access_token({"user_id": user.id})
    return {"access_token": token}
    
def get_user_by_id(id, db:Session):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user

def create_user(user, db: Session):
       # new_post = post_model(
    #     title=post.title, content=post.content, published=post.published, rating=post.rating)
    user_exits = db.query(User).filter(User.email == user.email).first()
    if user_exits:
        raise HTTPException(status_code=status.HTTP_208_ALREADY_REPORTED, detail="Email already exists" )
    new_user = User(**user.dict())
    new_user.password = hash_password(new_user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def delete_user(id, db :Session):
    post = db.query(User).filter(User.id == id)
    if post.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    post.delete(synchronize_session=False)
    db.commit()
    
    return {"message" :"User successfully deleted", "status":status.HTTP_204_NO_CONTENT}

# def update_user(id, updated_post, db :Session):
#     post_query =db.query(Post).filter(Post.id == id)
#     post = post_query.first()
    
#     if post is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    
#     post_query.update(updated_post.dict(),synchronize_session=False)
#     db.commit()    
#     return post