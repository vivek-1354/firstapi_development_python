from typing import Optional
from fastapi import FastAPI, HTTPException, status
from fastapi.params import Body
from pydantic import BaseModel
from uuid import uuid1 as u
from dummy_data import post_data
from uuid import uuid4 as u
import psycopg2
from psycopg2.extras import RealDictCursor

password = "V1v2ekmr@"


app = FastAPI()


class Post(BaseModel):
    title:str
    content:str
    published:bool = True
    rating: Optional[int] = None
    
while True:
    try:
        conn = psycopg2.connect(port=5434,host='localhost',database="fastapi", user="postgres",
                                password="V1v2ekmr@", cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was successfull!")
        break  
    except Exception as error:
        print("Failed to connect to database.")
        print("error : ", error)
        break
    
def find_post_by_id(id):
    cursor.execute("""SELECT * FROM posts WHERE post_id = %s """,(id,))
    new_post = cursor.fetchone()
    return new_post


@app.get('/')
async def root():
    return {"message":f"Hello Welcome...."}

@app.get('/posts')
def get_posts():
    query = "SELECT * FROM posts;"
    cursor.execute(query)
    products = cursor.fetchall()
    return {"data":products}

@app.get('/posts/{id}')
def get_posts(id:int):
    response = find_post_by_id(id)
    if response:
        return response
    raise HTTPException(status_code=404, detail="Post not found")

@app.post('/posts', status_code=status.HTTP_201_CREATED)
def create_post(post :Post):
    cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING * """,(post.title, post.content,post.published))
    new_post = cursor.fetchone()
    conn.commit()
    return {"message" : "successfully created.","data":new_post}


@app.delete("/posts/{id}")
def delete_post(id:int):
    cursor.execute("DELETE FROM posts WHERE post_id = %s RETURNING *",(id,))
    response = cursor.fetchone()
    conn.commit()
    if response is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    return {"message" :"post successfully deleted", "status":status.HTTP_204_NO_CONTENT}
    

@app.put("/posts/{id}")
def update_post(id : int, post:Post):
    cursor.execute("UPDATE posts SET title=%s, content=%s, published=%s, ratings=%s WHERE post_id = %s RETURNING *" ,(post.title, post.content, post.published, post.rating, id))
    response =cursor.fetchone()
    conn.commit()
    if response is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")    
    return {'message':"updated post","data":response}
    
