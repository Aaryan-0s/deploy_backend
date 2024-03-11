from passlib.context import CryptContext

pwd_crypt=CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash(password: str):
    return pwd_crypt.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_crypt.verify(plain_password, hashed_password)
