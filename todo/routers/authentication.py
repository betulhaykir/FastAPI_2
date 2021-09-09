from fastapi.security.oauth2 import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from todo import models
from fastapi import APIRouter, HTTPException,status
from fastapi.param_functions import Depends
from .. import schemas,database, token
from ..hashing import Hash
from sqlalchemy.orm import Session


router=APIRouter(
    tags=['Authentication']
)

@router.post('/login')
def login(request:OAuth2PasswordRequestForm= Depends(), db:Session =Depends(database.get_db)):
    user=db.query(models.User).filter(models.User.email==request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials")
    if not Hash.verify(user.password,request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Incorect passwprd")
    #    generate a jwt token and return

    access_token =token.create_access_token(
        data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
    