from fastapi import FastAPI,status
from src.crud.router.router import crud
from src.blog.router.router import blog
from src.convo.router.router import convo
from src.user.router.router import user
from src.auth.router.router import auth
from src.share.router.router import share


app=FastAPI()
app.include_router(crud)
app.include_router(blog)
app.include_router(convo)
app.include_router(user)
app.include_router(auth)
app.include_router(share)


@app.get(path="/",status_code=status.HTTP_200_OK)
async def entry_point()->dict:
    return {"message":"Hello World","status":status.HTTP_200_OK}




    