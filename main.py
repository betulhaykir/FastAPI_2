from typing import Optional, Text
from fastapi import FastAPI
from pydantic import BaseModel
#import uvicorn 

app= FastAPI()


@app.get('/todo')
async def index(limit=10, published:bool =True, sort: Optional[str]= None):
    #only get 10 published todos
    if published:
        return {"data": f'{limit} published todos from the db'}
    else:
        return {"data": f'{limit} todos from the db'}
@app.get('/todo/unpuplished')
def unpuplished():
    return {"data":"all unpuplished todos"}


@app.get('/todo/{id}')
def show(id: int):
    #fetch todo with id=id
    return {"data": id} 


@app.get('/todo/{id}/comments')
def comments(id, limit=10):
    #fetch comments of todo with id=id
    return limit
    return {"data":{'first comment','second comment'}}

class Todo(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post('/todo')
def create_todo(todo:Todo):
    return {"data": f"Todo is created with title as{todo.title}"}

#if __name__=="__main__":
 #   uvicorn.run(app,host="127.0.0.1",port=9000)