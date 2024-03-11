from fastapi import APIRouter,status
from src.convo.service.service import service


convo=APIRouter(prefix="/api/v1/convo",tags=["CONVO"])



@convo.get("/get",status_code=status.HTTP_200_OK)
async def crud_get(input: str):
    
    return service().get(input=input)
