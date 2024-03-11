
from fastapi import HTTPException
from src.entrypoint.database import get_db
from src.entrypoint.database import user
from src.crud.repository.crud_repository import CrudRepo
from sqlalchemy.orm import Session

class InMemoryRep:
    def __init__(self,db:Session):
        self.db=db
    def base_query(self):
        return self.db.query(CrudRepo)

    def add(self,item):
        item = CrudRepo(**item.__dict__)
        self.db.add(item)
        self.db.commit()
        self.db.refresh(item)
        
        return "added successfully"

    def update(self,change:CrudRepo):
       self.db.commit()
       self.db.refresh(change)
       return "updated successfully"  
            
       
        
        
        
    
    def get(self,index):
        return self.base_query().filter(CrudRepo.id==index).first()
    
    def getAll(self):
        
        return self.base_query().all()
    
    def delete(self,index):
        self.base_query().filter(CrudRepo.id==index).delete()  
        return "deleted successfully"

repo=InMemoryRep