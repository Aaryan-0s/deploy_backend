from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt


from src.user.schema.schemas import ResetTokenData, TokenData
SECRET_KEY = "d3"
ALGORITHM= "HS256"
ACESS_TOKEN_EXPIRE_MINUTES = 30 
FORGET_PWD_SECRET_KEY="d3"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/users/login")


def create_reset_password_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    token = jwt.encode(to_encode, FORGET_PWD_SECRET_KEY, ALGORITHM)
    return token

def create_access_token(data:dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    encoded_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token:str,credentials_exception):
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        userid: str = payload.get("id")
        username: str = payload.get("username")
        
        if userid is None:
            raise credentials_exception
        token_data = TokenData(id=userid,username=
                               username)
    except JWTError:
        raise credentials_exception
    return token_data



def verify_reset_token(token:str):
    print(token)
    payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
    print(payload)
        
    email: str = payload.get("email")
        
        
    token_data = ResetTokenData(email=
                               email)
    
    return token_data

def get_current_user(token:str=Depends(oauth2_scheme)):
    
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate":"Bearer"}
    )
    return verify_token(token,credentials_exception)


