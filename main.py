from typing import Optional
from fastapi import FastAPI, HTTPException, status
from fastapi.params import Body
from pydantic import BaseModel
from uuid import uuid1 as u
from dummy_data import post_data
from uuid import uuid4 as u


app = FastAPI()


class Post(BaseModel):
    title:str
    content:str
    published:bool = True
    rating: Optional[int] = None


@app.get('/')
async def root():
    return {"message":f"Hello Welcome...."}

@app.get('/posts')
def get_posts():
    return {"data":post_data}

@app.get('/posts/{id}')
def get_posts(id:str):
    for post in post_data:
        if str(post["id"]) == id:
            return {"singlePost": post}
    raise HTTPException(status_code=404, detail="Post not found")

@app.post('/posts', status_code=status.HTTP_201_CREATED)
def create_post(post :Post):
    new_post = post.model_dump()
    new_post["id"] = u()
    post_data.append(new_post)
    print(post.dict())
    return {"message" : "successfully created.","data":new_post}

def find_post_idx(id):
    print(type(id),id)
    for i,post in enumerate(post_data):
        if str(post["id"]) == id:
            return i

@app.delete("/posts/{id}")
def delete_post(id:str):
    idx = find_post_idx(id)
    if idx is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    post_data.pop(idx)
    return {"message" :"post successfully deleted", "status":status.HTTP_204_NO_CONTENT}
    

@app.put("/posts/{id}")
def update_post(id : str, post:Post):
    idx = find_post_idx(id)
    if idx is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    
    post_dict = post.model_dump()
    post_dict['id'] = id
    post_data[idx] = post_dict
    return {'message':"updated post","data":post_dict}
    
