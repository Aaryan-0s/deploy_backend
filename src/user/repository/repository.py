
from fastapi import HTTPException
from src.entrypoint.database import get_db
from src.entrypoint.database import user
from src.user.repository.user_repository import UserRepo
from sqlalchemy.orm import Session
from src.user.utils.utils import verify_password


from src.user.utils.oauth2 import create_access_token

class InMemoryRep:
    def __init__(self,db:Session):
        self.db=db
    def base_query(self):
        return self.db.query(UserRepo)

    def add(self,item):
        
        item = UserRepo(**item.__dict__)
        self.db.add(item)
        self.db.commit()
        self.db.refresh(item)
        
        return item


    
    def get(self,index):
        return self.base_query().filter(UserRepo.id==index).first()
    
    def getAll(self):
        
        return self.base_query().all()
    def login(self,data):
        user = self.base_query().filter(UserRepo.username==data.username).first()
        if not user:
            raise HTTPException(status_code=404,detail="User not found")
        print(data.password)
        if not verify_password(data.password,user.password):
            raise HTTPException(status_code=404,detail="Incorrect password")
        
        access_token = create_access_token(data={"username":user.username})  
        return {"access_token":access_token,"token_type":"bearer"}
    
    

repo=InMemoryRep