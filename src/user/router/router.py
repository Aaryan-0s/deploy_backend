
from fastapi import APIRouter, Depends,status
from sqlalchemy.orm import Session

from src.entrypoint.database import get_db
from src.user.service.service import service    
from src.user.model.model import User,UserOut,UserLogin,Token
from src.user.utils.utils import hash
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

from src.user.utils.oauth2 import get_current_user



user=APIRouter(prefix="/api/v1/user",tags=["User"])

@user.get("/get",status_code=status.HTTP_200_OK,response_model=UserOut)
async def user_get(index:int,db:Session=Depends(get_db)):
    
    return service(db).get(index=index)
@user.get("/getAll",status_code=status.HTTP_200_OK,response_model=list[UserOut])
async def user_getAll(db:Session=Depends(get_db),get_current_user:str=Depends(get_current_user)):
   
    return service(db).getAll()

@user.post("/add",status_code=status.HTTP_200_OK,response_model=UserOut)
async def user_post(data:User,db:Session=Depends(get_db)):
    hashed_Passwd=hash(data.password)
    data.password=hashed_Passwd
    return service(db).add(data=data)

@user.post("/login",status_code=status.HTTP_200_OK,response_model=Token)
async def user_post(data:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    

    return service(db).login(data=data)