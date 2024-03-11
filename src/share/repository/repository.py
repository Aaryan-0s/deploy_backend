
from fastapi import HTTPException
from src.entrypoint.database import get_db
from src.entrypoint.database import user
from src.share.repository.share_repository import ShareRepo
from sqlalchemy.orm import Session





class InMemoryRep:
    def __init__(self,db:Session):
        self.db=db
    def base_query(self):
        return self.db.query(ShareRepo)

   
    
    def get(self,index):
        return self.base_query().filter(ShareRepo.id==index).first()
    
    def Load(self):
        
        return self.base_query().all()
  
    

repo=InMemoryRep