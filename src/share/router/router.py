
from fastapi import APIRouter, Depends,status
from sqlalchemy.orm import Session

from src.entrypoint.database import get_db
from src.share.service.service import service    
from src.share.model.model import ShareOut
from src.user.utils.oauth2 import get_current_user







share=APIRouter(prefix="/api/v1/share",tags=["Share"])

@share.get("/get",status_code=status.HTTP_200_OK,response_model=ShareOut)
async def share_get(index:int,db:Session=Depends(get_db),get_current_user:str=Depends(get_current_user)):
    print(get_current_user)
    
    return service(db).get(index=index)

@share.get("/load",status_code=status.HTTP_200_OK,response_model=list[ShareOut])
async def share_load(db:Session=Depends(get_db)):
    
    return service(db).load()