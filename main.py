from typing import Optional
from fastapi import FastAPI, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from uuid import uuid1 as u


app = FastAPI()


class Post(BaseModel):
    title:str
    content:str
    published:bool = True
    rating: Optional[int] = None

from uuid import uuid4 as u

data = [
    {"id": u(), "title": "Top beaches", "content": "Check out all the awesome beaches", "published": True, "ratings": 545},
    {"id": u(), "title": "Mountain Escapes", "content": "Breathe the fresh mountain air", "published": True, "ratings": 678},
    {"id": u(), "title": "City Life", "content": "Explore vibrant urban spots", "published": False, "ratings": 412},
    {"id": u(), "title": "Hidden Waterfalls", "content": "Find secret falls off the grid", "published": True, "ratings": 329},
    {"id": u(), "title": "Desert Adventures", "content": "Ride the dunes under the stars", "published": True, "ratings": 258},
    {"id": u(), "title": "Historical Sites", "content": "Step into the past at these places", "published": False, "ratings": 334},
    {"id": u(), "title": "Island Retreats", "content": "Unplug and relax in paradise", "published": True, "ratings": 721},
    {"id": u(), "title": "Cultural Tours", "content": "Experience rich local traditions", "published": True, "ratings": 489},
    {"id": u(), "title": "Foodie Heaven", "content": "Eat your way around the world", "published": True, "ratings": 901},
    {"id": u(), "title": "Wildlife Safaris", "content": "See nature up close and personal", "published": False, "ratings": 384},
    {"id": u(), "title": "Coastal Drives", "content": "Road trip along the sea", "published": True, "ratings": 223},
    {"id": u(), "title": "Camping Spots", "content": "Find the best places to pitch a tent", "published": True, "ratings": 317},
    {"id": u(), "title": "Snowy Peaks", "content": "Shred the slopes this season", "published": True, "ratings": 600},
    {"id": u(), "title": "River Rafting", "content": "Ride the rapids like a pro", "published": False, "ratings": 198},
    {"id": u(), "title": "Jungle Treks", "content": "Adventure deep in the wild", "published": True, "ratings": 443},
    {"id": u(), "title": "Lakeside Views", "content": "Peaceful scenes by the lake", "published": True, "ratings": 567},
    {"id": u(), "title": "Road Less Traveled", "content": "Underrated destinations to explore", "published": False, "ratings": 321},
    {"id": u(), "title": "Sunset Spots", "content": "Catch the best golden hour scenes", "published": True, "ratings": 404},
    {"id": u(), "title": "Forest Cabins", "content": "Cozy getaways in the woods", "published": True, "ratings": 289},
    {"id": u(), "title": "Global Festivals", "content": "Dance, eat, and celebrate worldwide", "published": False, "ratings": 699}
]


@app.get('/')
async def root():
    return {"message":f"Hello Welcome...."}


@app.get('/posts')
def get_posts():
    return {"data":data}

@app.get('/posts/{id}')
def get_posts(id:str):
    for post in data:
        if str(post["id"]) == id:
            return {"singlePost": post}
    raise HTTPException(status_code=404, detail="Post not found")

@app.post('/posts')
def create_post(post :Post):
    new_post = post.model_dump()
    new_post["id"] = u()
    data.append(new_post)
    print(post.dict())
    return {"message" : "successfully created.","data":data}


