from typing import Text, Optional
from fastapi import FastAPI
from datetime import datetime
from pydantic import BaseModel

app = FastAPI()

postdb = []


class Post(BaseModel):
    id: int
    title: str
    author: str
    content: Text
    created_at: datetime = datetime.now()
    published_at: datetime
    published: Optional[bool] = False


@app.get("/allpost")
def get_posts():
    return postdb


@app.post("/post")
def add_post(post: Post):
    postdb.append(post.dict())
    return postdb[-1]


@app.get("/post/{post_id}")
def get_post(post_id: int):
    post = post_id - 1
    return postdb[post]

# Teste de Coment


@app.post("/post/{post_id}")
def update_post(post_id: int, post: Post):
    postdb[post_id] = post
    return {"message": "Post has been updated succesfully"}


@app.delete("/post/{post_id}")
def delete_post(post_id: int):
    postdb.pop(post_id-1)
    return {"message": "Post has been deleted succesfully"}


@app.get("/")
def read_root():
    return {"home": "Hello World"}
