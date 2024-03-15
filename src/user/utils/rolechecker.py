
from fastapi import Depends, HTTPException,status
from requests import Session
from src.entrypoint.database import get_db
from src.user.schema import schemas




from src.user.service.services import UserServices
from src.user.utils.oauth2 import get_current_user


def is_verified( db:Session=Depends(get_db), current_user:schemas.User=Depends(get_current_user)):
   user= current_user
   user_services = UserServices(db)
   response = user_services.is_verified(user)
   return response

class RoleChecker:
  def __init__(self, allowed_roles):
    self.allowed_roles = allowed_roles
     

  def __call__(self,user:schemas.UserType=Depends(is_verified) ):
    print(user)
    if user.usertype in self.allowed_roles:
      return user
    raise HTTPException(
status_code=status.HTTP_401_UNAUTHORIZED, 
detail="You don't have enough permissions")