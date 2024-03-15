from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException,status
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session



from src.entrypoint.database import get_db
from src.user.schema import schemas
from src.user.service.services import UserServices
from src.address.service.service import AddressServices
from src.user.utils.oauth2 import get_current_user
from starlette.background import BackgroundTasks

from src.user.utils.rolechecker import RoleChecker






user = APIRouter(prefix='/api/users', tags=['User'])



@user.post('/signup', response_model=schemas.User)
def create_user(user:schemas.UserCreate, db:Session=Depends(get_db)):
    user_services = UserServices(db)
    new_user = user_services.create_user(user)
    return new_user



@user.post('/login',status_code=status.HTTP_200_OK ,response_model=schemas.Token)
async def login_user(data:OAuth2PasswordRequestForm = Depends(), db:Session=Depends(get_db)):
    user_services = UserServices(db)
    print(data)
    user = user_services.login_user(user_data=data)
    return user



@user.get('/verification-code')
def get_verification_code(db:Session=Depends(get_db), current_user : schemas.Token=Depends(get_current_user)):
    user_id = current_user.id
    user_services = UserServices(db)
    resp = user_services.send_verification_code(user_id=user_id)
    if resp: return JSONResponse(status_code=200, content="Verification Code sent")
    
    
    
@user.post('/verify-email')
def verify_user_email(code:int, db:Session=Depends(get_db), current_user:schemas.Token=Depends(get_current_user)):
    user_services = UserServices(db)
    user_id = current_user.id
    resp = user_services.verify_email(user_id=user_id, code=code)
    if resp == True:
        return JSONResponse(
            status_code=200,
            content="User Successfully verified"
        )
    
    
    
@user.get('/', response_model=schemas.User)
def get_other_users(id:int|None=None, username:str|None=None, db:Session=Depends(get_db)):
    user_services = UserServices(db)
    query = schemas.UserBrowse(id=id, username=username)
    user_info = user_services.browse_other_users(query=query)
    return user_info
    
    
    
@user.get('/me',status_code=status.HTTP_200_OK, response_model=schemas.User)
def get_user_by_id( db:Session=Depends(get_db), get_current_user:schemas.UserType=Depends(RoleChecker(allowed_roles=["user"]))):
    
    user_services = UserServices(db)
    user = user_services.get_user_by_id(get_current_user.id)
    return user



@user.delete('/me',status_code=status.HTTP_200_OK, response_model=schemas.User,)
def delete_current_user( db:Session=Depends(get_db),get_current_user:schemas.TokenData=Depends(get_current_user)):
    print(get_current_user)
    user_services = UserServices(db)
    user = user_services.deactivate(get_current_user.id)
    return user



@user.put('/me',status_code=status.HTTP_200_OK, response_model=schemas.User,)
def update_current_user( profile_update:schemas.UserUpdate,db:Session=Depends(get_db),get_current_user:schemas.TokenData=Depends(get_current_user)):

    user_services = UserServices(db)
    updated_user = user_services.user_update(profile_update, get_current_user.id)
    return updated_user



@user.post("/forget-password",status_code=status.HTTP_200_OK, )
async def forget_password( email: schemas.ForgetPasswordRequest,db: Session = Depends(get_db)):
    user_services = UserServices(db)
  
    response = user_services.forget_password(email)
   
    return response
    
    
    
@user.post("/reset-password",status_code=status.HTTP_200_OK)
async def forget_password( reset_password:schemas.ResetPassword,db: Session = Depends(get_db)):
    user_services = UserServices(db)
   
   
    response = user_services.reset_password(reset_password)
   
    return response



@user.put('/me/change-password',status_code=status.HTTP_200_OK, )
def change_password( password:schemas.PasswordChange,db:Session=Depends(get_db),get_current_user:schemas.TokenData=Depends(get_current_user)):
    user_services = UserServices(db)
    print(get_current_user.id)
    response = user_services.change_password( get_current_user.id,password)
    return response



@user.get('/{user_id}/address', response_model=schemas.UserAddress,)
def get_user_address( db:Session=Depends(get_db), current_user:schemas.Token=Depends(get_current_user)):
    addres_service = AddressServices(db)
    address = addres_service.get_user_address(user_id=current_user.id)
    return address
    
    



@user.post('/isadmin')
def is_admin( db:Session=Depends(get_db) ,current_user:schemas.UserType=Depends(RoleChecker(allowed_roles=["admin","user"]))):
    user_services = UserServices(db)
    return {"usertype":"admin"}


@user.put("/assign-agents")
def assign_agents( agent_id:int,db:Session=Depends(get_db) ,current_user:schemas.UserType=Depends(RoleChecker(allowed_roles=["admin"]))):
    user_services = UserServices(db)
    response=user_services.assign_agent(agent_id)
    return response;


@user.put("/assign-admin")
def assign_agents( user_id:int,db:Session=Depends(get_db) ,current_user:schemas.UserType=Depends(RoleChecker(allowed_roles=["admin"]))):
    user_services = UserServices(db)
    response=user_services.assign_admin(user_id)
    return response;








   
   
   

   