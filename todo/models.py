from sqlalchemy import Column,Integer,String,Boolean
from sqlalchemy.sql.schema import ForeignKey
from .database import Base
from sqlalchemy.orm import relationship


class Todo(Base):
    __tablename__='todos'
    
    id = Column(Integer,primary_key=True, index=True)
    description=Column(String)
    due_date=Column (String)
    user_id=Column(Integer,ForeignKey('users.id'))

    creator= relationship("User", back_populates="todos")


class User(Base):
    __tablename__='users'

    id = Column(Integer,primary_key=True, index=True)
    name=Column(String)
    email=Column (String)
    password= Column (String)

    todos= relationship("Todo", back_populates="creator")