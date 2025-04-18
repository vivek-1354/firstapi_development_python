from typing import Optional
from fastapi import FastAPI, HTTPException, status, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from models import post_model
from models.post_model import Post as Post_Schema


from database import engine, get_db

post_model.Base.metadata.create_all(bind=engine)


app = FastAPI()


class Post(BaseModel):
    title:str
    content:str
    published:bool = True
    rating: Optional[int] = None
    
    
@app.get('/')
def root():
    return {"message":f"Hello Welcome...."}

@app.get('/posts')
def get_posts(db:Session  = Depends(get_db)):
    posts = db.query(Post_Schema).all()
    return {"data" :posts}

@app.get('/posts/{id}')
def get_posts(id:int, db:Session  = Depends(get_db)):
    response = db.query(Post_Schema).get({"id":id})
    if response:
        return response
    raise HTTPException(status_code=404, detail="Post not found")

@app.post('/posts', status_code=status.HTTP_201_CREATED)
def create_post(post :Post, db:Session  = Depends(get_db)):
    # new_post = Post_Schema(
    #     title=post.title, content=post.content, published=post.published, rating=post.rating)
    new_post = Post_Schema(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return {"message" : "successfully created.","data":new_post}



@app.delete("/posts/{id}")
def delete_post(id:int, db:Session  = Depends(get_db)):
    post = db.query(Post_Schema).filter(Post_Schema.id == id)
    if post.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    post.delete(synchronize_session=False)
    db.commit()
    
    return {"message" :"post successfully deleted", "status":status.HTTP_204_NO_CONTENT}
    

@app.put("/posts/{id}")
def update_post(id : int, updated_post:Post, db:Session  = Depends(get_db)):
    post_query =db.query(Post_Schema).filter(Post_Schema.id == id)
    post = post_query.first()
    
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    
    post_query.update(updated_post.dict(),synchronize_session=False)
    db.commit()    
    return {'message':"updated post","data":'successful'}
    
