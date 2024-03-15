from pydantic import BaseModel, EmailStr, validator

from datetime import datetime

class ResetForgetPassword(BaseModel):
    secret_token: str
    new_password: str
    confirm_password: str

class SuccessMessage(BaseModel):
    success: bool
    status_code: int
    message: str


class UserBase(BaseModel):
    username: str
    email : EmailStr

class ForgetPasswordRequest(BaseModel):
    email: str
class UserType(UserBase):
    id:int
    usertype:str
    
class ResetPassword(BaseModel):
    token: str
    new_password: str
 

class UserCreate(UserBase):
    password : str

class UserActivity(UserBase):
    is_active : bool
    is_verified : bool
    modified_by : int | None = None
    modified_on : datetime | None = None



class UserToDB(UserBase):
    hashed_password : str

# Response Model
class User(UserBase):
    id : int
    first_name : str | None = None
    last_name : str | None = None
    address_id : int | None = None
    is_active : bool
    is_verified : bool
    created_by : str
    created_on : datetime
    
    class Config:
        from_attributes = True

class UserUpdate(BaseModel):
    first_name : str | None = None
    last_name : str | None = None
    username : str | None = None
    email : EmailStr | None = None
 
 
class UserBrowse(BaseModel):
    id : int | None = None
    username : str | None = None
    email : str | None = None
        
        
class UserLogin(BaseModel):
  
    username : str
    password : str


class PasswordChange(BaseModel):
    old_password : str
    new_password : str


class Token(BaseModel):
    access_token : str |None=None
    token_type:str|None=None




class UserAddress(BaseModel):
    province_name : str | None = None
    district_name : str | None = None
    municipality_name : str | None = None
    ward : int | None = None
    tole : str | None = None


class TokenData(BaseModel):
    username: str | None=None
    id: int | None=None
    # class Config:
    #     orm_mode=True
    

    
class MailBody(BaseModel):
    to: str
    subject: str
    body: str


class ResetTokenData(BaseModel):
    email: str | None=None
