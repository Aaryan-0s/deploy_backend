from fastapi import APIRouter, Depends,status
from src.entrypoint.database import get_db
from src.crud.service.service import service
from src.crud.model.model import User
from sqlalchemy.orm import Session

crud=APIRouter(prefix="/api/v1/crud",tags=["CRUD"])



@crud.get("/get",status_code=status.HTTP_200_OK)
async def crud_get(index:int,db:Session=Depends(get_db)):
    
    return service(db).get(index=index)
@crud.get("/getAll",status_code=status.HTTP_200_OK)
async def crud_getAll(db:Session=Depends(get_db)):
    
    return service(db).getAll()

@crud.post("/add",status_code=status.HTTP_200_OK)
async def crud_post(data:User,db:Session=Depends(get_db)):
    return service(db).add(data=data)


@crud.put("/update",status_code=status.HTTP_200_OK)
async def crud_put(index:int,data:User,db:Session=Depends(get_db)):
    updateUser=data.model_dump(exclude_unset=True)
           
    return service(db).update(index=index,data=updateUser)


@crud.delete("/delete",status_code=status.HTTP_200_OK)
async def crud_delete(index:int,db:Session=Depends(get_db)):
    return service(db).delete(index=index)