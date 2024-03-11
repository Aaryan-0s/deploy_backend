
from pydantic import BaseModel
from typing import Optional


class ShareOut(BaseModel):
    Company: str | None=None
    LTP: str | None=None
    CHG: str | None=None
    CHG_percent: str | None=None
    HIGH: str | None=None
    LOW: str | None=None
    Open: str | None=None
    Quantity: str | None=None
    txn: str | None=None
    class Config:
        orm_mode=True
    

    
    
    
    
   
