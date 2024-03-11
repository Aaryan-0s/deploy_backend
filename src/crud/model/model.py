
from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    username: str | None=None
    email: str | None=None
    firstname: str | None=None
    lastname: str | None=None
    dob: str | None=None
    gender: str | None=None


