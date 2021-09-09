
from todo.routers import authentication
from fastapi import FastAPI
from .import models
from .database import engine
from .routers import todo, user

app=FastAPI()

models.Base.metadata.create_all(engine)


app.include_router(authentication.router)
app.include_router(todo.router)
app.include_router(user.router)
