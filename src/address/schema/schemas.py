from pydantic import BaseModel, EmailStr, validator

from datetime import datetime



class UserAddress(BaseModel):
    province_name : str | None = None
    district_name : str | None = None
    municipality_name : str | None = None
    ward : int | None = None
    tole : str | None = None


class AddressBase(BaseModel):
    municipality_id : int
    ward : int | None = None
    tole : str | None = None
    remarks : str | None = None
    
    
    @validator('ward')
    def check_ward(cls, v):
        if v is not None and v<=0:
            raise ValueError('Ward must be positive num')
        return v
class AddressCreate(AddressBase):
    pass    


# Response Model
class Address(AddressBase):
    id : int
    modified_on : datetime | None = None
    
    class Config:
        from_attributes = True
        
        
class AddressUpdate(AddressBase):
    municipality_id : int | None = None
    remarks : str | None = None
    modified_on : datetime = datetime.now()

    


    
class Province(BaseModel):
    id : int
    name : str
    created_on : datetime
    

class District(BaseModel):
    id : int
    name : str
    province_id : int
    created_on : datetime
    
    

class Municipality(BaseModel):
    id : int
    name : str
    num_of_ward : int
    district_id : int
    created_on : datetime
