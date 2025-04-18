from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models.post import Post

def get_all_posts(db:Session):
    return db.query(Post).all()
    
def get_post_by_id(id, db:Session):
    post = db.query(Post).filter(Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    return post

def create_post(post, db: Session):
       # new_post = post_model(
    #     title=post.title, content=post.content, published=post.published, rating=post.rating)
    new_post = Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

def delete_post(id, db :Session):
    post = db.query(Post).filter(Post.id == id)
    if post.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    post.delete(synchronize_session=False)
    db.commit()
    
    return {"message" :"post successfully deleted", "status":status.HTTP_204_NO_CONTENT}

def update_post(id, updated_post, db :Session):
    post_query =db.query(Post).filter(Post.id == id)
    post = post_query.first()
    
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    
    post_query.update(updated_post.dict(),synchronize_session=False)
    db.commit()    
    return post