from sqlalchemy.orm import Session


from src.user.model.models import User, VerificationCode
from src.user.schema.schemas import UserLogin, UserToDB, UserUpdate
from src.user.utils.oauth2 import create_access_token

class UserRepo():
    
    def __init__(self, db:Session):
        self.db = db
        
        
    def fetch_all_users(self):
        return self.db.query(User).all()
        
    def fetch_user_by_id(self, user_id:int):
        return self.db.query(User).filter(User.id == user_id).first()
    
    def fetch_user_by_username(self, username:str):
        return self.db.query(User).filter(User.username == username).first()
    
    def fetch_user_by_email(self, email:str):
        return self.db.query(User).filter(User.email == email).first()
    

    def deactivate_user(self, id:int):
        user = self.db.query(User).filter(User.id == id).first()
        user.is_active = False
        self.db.commit()
        self.db.refresh(user)
        return user
        
    def assign_agent(self,id:int):
        user = self.db.query(User).filter(User.id == id).first()
        user.usertype = "agent"
        self.db.commit()
        self.db.refresh(user)
        return user
    
    def assign_admin(self,id:int):
        user = self.db.query(User).filter(User.id == id).first()
        user.usertype = "admin"
        self.db.commit()
        self.db.refresh(user)
        return user
    
    def save_changes(self, data):
        self.db.add(data)
        self.db.commit()
    

    def user_update(self, data:UserUpdate):
        self.db.commit()
        self.db.refresh(data)
        return data


    
    def create_new_user(self, user:UserToDB):
        print(user)
        print(user.model_dump())
        new_user = User(**user.model_dump())
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user
    
    def Create_token(self, user_data:UserLogin,id:int):
        print(user_data)
        access_token = create_access_token(data={"id": id,"username":user_data.username})
        return {"access_token": access_token, "token_type": "bearer"}
    
    def mark_as_verified(self, user_id:int):
        user = self.db.query(User).filter(User.id == user_id).first()
        if user:
            user.is_verified = True
            self.db.commit()
            return True
    def save_new_password(self, user:User, new_password:str):
        
        user.hashed_password = new_password
        self.db.commit()
        self.db.refresh(user)
        return user
    
    
class VerificationRepo():
    def __init__(self, db:Session):
        self.db = db
        
    def get_verification_code(self, user_id):
        verification_code = self.db.query(VerificationCode).filter(VerificationCode.user_id==user_id).first()
        # verification_code = self.db.query(VerificationCode).filter(VerificationCode.user_id==user_id).first()
        return verification_code
        
    def save_new_verification_code(self, user_id:int, code:int, expiration_date):
        new_code = VerificationCode(user_id=user_id, code=code, expiration_date=expiration_date)
        self.db.add(new_code)
        self.db.commit()
        self.db.refresh(new_code)
        return new_code
        
    def update_verification_code(self, old_code, code:int, expiration_date):
        old_code.code = code
        old_code.expiration_date = expiration_date
        self.db.commit()
        self.db.refresh(old_code)
        return old_code
    
    
    def delete_verification_code(self,user_id:int):
        verification_code = self.get_verification_code(user_id=user_id)
        if verification_code:
            self.db.delete(verification_code)
            self.db.commit()
            return True
        
        
    