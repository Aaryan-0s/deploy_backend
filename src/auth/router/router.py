from fastapi import APIRouter
from src.auth.service.service import AuthService

auth=APIRouter(
    prefix="/auth",
    tags=["AUTH"]
)

@auth.get(path="/{token_id}")
async def auth_function():
    auth=AuthService.auth_function
    return auth