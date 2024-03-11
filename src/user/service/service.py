from src.user.repository.repository import repo
from sqlalchemy.orm import Session
from src.user.utils.oauth2 import create_access_token
class UserService:
    def __init__(self,db:Session):
        self.repo=repo(db)

    def get(self,index):
        msg=self.repo.get(index=index)
        return msg
    def getAll(self):
        msg=self.repo.getAll()
        return msg

    def add(self,data):
      
        return self.repo.add(item=data)
    
    def login(self,data):
      
        return self.repo.login(data=data)
    


    


service=UserService