
from src.share.repository.repository import repo
from sqlalchemy.orm import Session

class ShareService:
    def __init__(self,db:Session):
        self.repo=repo(db)

    def get(self,index):
        
        msg=self.repo.get(index=index)
        return msg
    def load(self):
        
        
        msg=self.repo.load()
        return msg

  
    


    


service=ShareService