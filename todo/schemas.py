from fastapi.param_functions import Body
from pydantic import BaseModel
from typing import List
from typing import Optional

class TodoBase(BaseModel):
    title: str
    body: str

class Todo(TodoBase):
    class Config():
        orm_mode=True 


class User(BaseModel):
    name: str
    email: str
    password:str

class ShowUser(BaseModel):
    title: str
    body: str
    todos:List[Todo]=[]
    class Config():
        orm_mode=True

class ShowTodo(BaseModel):
    title: str
    body: str
    creator: ShowUser

    class Config():
        orm_mode=True

class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None