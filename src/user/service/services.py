import random
from datetime import timedelta
from datetime import datetime as DT
from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session


from src.user.schema.schemas import PasswordChange, ResetPassword, UserBrowse, UserCreate, UserLogin, UserToDB, User, UserUpdate
from src.user.repository.repository import UserRepo, VerificationRepo
from src.user.utils.utils import *

from src.user.service.email_services import send_reset_password_email, send_verification_email
from src.user.utils.oauth2 import create_reset_password_token, verify_reset_token



class UserServices():
    
    def __init__(self, db:Session):
        self.repo = UserRepo(db)
        # self.verification_repo = VerificationRepo(db)
        self.verification_service = VerificationService(db)
    
    def get_user_by_id(self, user_id:int):
        user = self.repo.fetch_user_by_id(user_id)
        if user is None:
            raise HTTPException(
                status_code = status.HTTP_400_BAD_REQUEST,
                detail = "Invalid user Id"
            )
        return user
    
    def is_verified(self, user:User):
        user=self.get_user_by_id(user.id)
        if(user.is_verified == False):
            raise HTTPException(
                status_code = status.HTTP_400_BAD_REQUEST,
                detail = "User not verified"
            )
        return user
    
    def get_user_by_email(self, email:int):
        user = self.repo.fetch_user_by_email(email)
        if user is None:
            raise HTTPException(
                status_code = status.HTTP_400_BAD_REQUEST,
                detail = "Invalid email"
            )
        return user
        
    def get_user_by_username(self, username:str):
        user = self.repo.fetch_user_by_username(username)
        if user is None:
            raise HTTPException(
                status_code = status.HTTP_400_BAD_REQUEST,
                detail = "Invalid Username"
            )
        return user
    
    
    
    def save_address_id(self, user_id, address_id):
        user = self.repo.fetch_user_by_id(user_id=user_id)
        user.address_id = address_id
        self.repo.save_changes(user)
        return True
    
    def assign_agent(self, user_id):
        user = self.repo.fetch_user_by_id(user_id=user_id)
        print(user_id)
        if user.usertype == "agent":
            raise HTTPException(status_code=400, detail="User is already an agent")
        self.repo.assign_agent(user_id)
        return {"message":"Agent assigned successfully"}
    
    def assign_admin(self, user_id):
        user = self.repo.fetch_user_by_id(user_id=user_id)
        print(user_id)
        if user.usertype == "admin":
            raise HTTPException(status_code=400, detail="User is already an admin")
        self.repo.assign_admin(user_id)
        return {"message":"Admin assigned successfully"}
    
    
    def user_update(self, user_data:UserUpdate, userid:str):
       
       data=self.repo.fetch_user_by_id(userid)
       user_data= user_data.model_dump(exclude_unset=True)

       for(key,value) in user_data.items():
          setattr(data,key,value)
       return self.repo.user_update(data)
    
    def change_password(self, user_id:int, password:PasswordChange):
       
        user = self.get_user_by_id(user_id)
        
        if not verify_password(password.old_password, user.hashed_password):
            raise HTTPException(status_code=400, detail="Invalid old password")
        hashed_password = hash_password(password.new_password)
        self.repo.save_new_password(user, hashed_password)
        return {"message":"Password changed successfully"}

       
       

    

    def create_user(self, user_data:UserCreate):
        # Check if Username is available
        user_username = self.repo.fetch_user_by_username(user_data.username)
        if user_username is not None:
            raise HTTPException(status_code = 400, detail = "User with username already exist")

        # Check if email is available
        user_email = self.repo.fetch_user_by_email(user_data.email)
        if user_email is not None:
            raise HTTPException(status_code = 400, detail = "User with email already exist")
        
        hashed_password = hash_password(user_data.password)
        user = UserToDB(**user_data.model_dump(), hashed_password=hashed_password)
        
        new_user = self.repo.create_new_user(user)
        code = self.send_verification_code(new_user.id)
        return new_user
    

    def login_user(self,user_data:UserLogin):
        print("executed")
        user= self.repo.fetch_user_by_username(user_data.username)
        if user is None:
            raise HTTPException(status_code = 400, detail = "Invalid Username")
        if not verify_password(user_data.password, user.hashed_password) :
            raise HTTPException(status_code = 400, detail = "Invalid Password Or Username")
    
        return self.repo.Create_token(user_data,user.id)
    
    def send_verification_code(self, user_id):
        user = self.get_user_by_id(user_id)
        if user.is_verified is False:
            code = self.verification_service.generate_and_save_code(user_id=user.id)
            send_verification_email(user=user, code=code)
            return True
        raise HTTPException(status_code=400, detail="User already verified")
    

    def deactivate(self, id:int):
        user = self.get_user_by_id(id)
        if user.is_active is False:
            raise HTTPException(status_code=400, detail="User already deactivated")
        self.repo.deactivate_user(id)
        return user
    
    def browse_other_users(self, query:UserBrowse):
        if query.id:
            user = self.get_user_by_id(user_id=query.id)
            return user
        if query.username:
            user = self.get_user_by_username(username=query.username)
            return user
        else:
            raise HTTPException(status_code=400, detail="Bad request")
    
    
    def verify_email(self, user_id:int, code):
        user = self.repo.fetch_user_by_id(user_id)
        
        if user and user.is_verified is False:
            saved_code = self.verification_service.get_unexpired_code(user_id=user_id)
            if saved_code != code:
                raise HTTPException(status_code=406, detail="Verification code didn't match")
            else:
                self.repo.mark_as_verified(user_id)
                self.verification_service.remove_verification_code(user_id=user_id)
                return True
                
        else:
            raise HTTPException(status_code=400,detail="User already verified!")
            
                
    def forget_password(self, email:str):
       
        user = self.repo.fetch_user_by_email(email.email)
        
        if user:
                token=create_reset_password_token(data={"email":user.email})
                send_reset_password_email(user=user, code=token)
               
                return True
        else:
                raise HTTPException(status_code=400, detail="User not found")
        

    def reset_password(self,data:ResetPassword):
        
        email=verify_reset_token(data.token)
        print(email)
        
        user = self.repo.fetch_user_by_email(email.email)
        if user:
            hashed_password = hash_password(data.new_password)
            print(hashed_password)
            
            self.repo.save_new_password(user, hashed_password)
            return True
        else:
            raise HTTPException(status_code=400, detail="User not found")


class VerificationService():
    
    def __init__(self, db:Session):
        self.repo = VerificationRepo(db)
    
    
    def get_unexpired_code(self, user_id:int):
        verification_code = self.repo.get_verification_code(user_id=user_id)
        if verification_code:
            print(DT.now())
            print(verification_code.expiration_date)
            if DT.now() <= verification_code.expiration_date:
                return verification_code.code
            raise HTTPException(status_code=400, detail="Verification code is expired.")
        return None
    
    
    def generate_and_save_code(self, user_id:int):
        code = random.randint(10000, 99999)
        created_on = DT.now()
        expiration_date = created_on + timedelta(minutes=30)
        
        old_code = self.repo.get_verification_code(user_id=user_id)
        if old_code is None:
            saved_item = self.repo.save_new_verification_code(user_id=user_id, code=code, expiration_date=expiration_date)
            return code
        else:
            saved_item = self.repo.update_verification_code(old_code=old_code, code=code, expiration_date=expiration_date)
            return code
    
    def remove_verification_code(self, user_id:int):
        self.repo.delete_verification_code(user_id=user_id)
        return True



