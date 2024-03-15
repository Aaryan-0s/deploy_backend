from fastapi import FastAPI,status


from src.entrypoint.database import check_db_connection
from src.user.router.router import user
from src.address.router.router import address

check_db_connection()

app=FastAPI()
app.include_router(user)
app.include_router(address)


@app.get(path="/",status_code=status.HTTP_200_OK)
def Homepage():
    return {"message":"hello world",
            "status":status.HTTP_200_OK}