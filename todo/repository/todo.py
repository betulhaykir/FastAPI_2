from sqlalchemy.orm.session import Session
from ..import models, schemas
from fastapi import HTTPException


def get_all(db:Session):
    todos= db.query(models.Todo).all()
    return todos

def create(request: schemas.Todo, db:Session):
    new_todo=models.Todo(title=request.title,body=request.body,user_id=1)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo


def destroy(id:int,db:Session):
    todo = db.query(models.Todo).filter(models.Todo.id==id)
    
    if not todo.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Todo with id{id} not found")
    
    todo.delete(synchronize_session=False)
    db.commit()
    return 'done'

def update(id:int,request:schemas.Todo,db:Session):
    todo= db.query(models.Todo).filter(models.Todo.id ==id)
    
    if not todo.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Todo with id{id} not found.")
    
    todo.update(request)
    db.commit()
    return 'updated'

def show(id:int,db:Session):
    todo = db.query(models.Todo).filter(models.Todo.id==id).first()
    if not todo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Todo with the id {id} is not available..")
        #response.status_code=status.HTTP_404_NOT_FOUND
        #return{"detail":f"Todo with the id {id} is not available.."}
    
    return todo
