

from fastapi import APIRouter


auth=APIRouter(
    prefix="/auth",
    tags=["AUTH"]
)

@auth.post(path="/token/{token_id}")
async def validate_token(token_id:str,q_params:str):
    return {
        "token id":token_id,
        "q":q_params
    }