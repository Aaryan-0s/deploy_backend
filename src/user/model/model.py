
from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    username: str | None=None
    email: str | None=None
    password: str | None=None

class UserOut(BaseModel):
    username: str | None=None
    email: str | None=None
class UserLogin(BaseModel):
    username: str | None=None
    password: str | None=None
    
    
class Token(BaseModel):
    access_token: str | None=None
    token_type: str | None=None
    

class TokenData(BaseModel):
    username: str | None=None
    class Config:
        orm_mode=True
    
    
    
    
   
