from src.user.repository.repository import repo
from sqlalchemy.orm import Session

class CrudService:
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
    
    

    


service=CrudService