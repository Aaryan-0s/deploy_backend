from fastapi import APIRouter, Depends,status
from sqlalchemy.orm import Session


from src.entrypoint.database import get_db
from src.address.schema import schemas
from src.user.schema.schemas import Token
from src.address.service.service import AddressServices
from src.user.utils.oauth2 import get_current_user


address = APIRouter(prefix='/api/addresses', tags=['Address'])




@address.post('/',status_code=status.HTTP_200_OK, response_model=schemas.Address,)
def add_address( data:schemas.AddressCreate,  db:Session=Depends(get_db), current_user:Token = Depends(get_current_user)):
    address_service = AddressServices(db)
    address = address_service.add_address(data=data, user_id=current_user.id)
    return address


@address.put('/',status_code=status.HTTP_200_OK, response_model=schemas.Address,)
def update_address( data:schemas.AddressUpdate, db:Session=Depends(get_db), current_user:Token = Depends(get_current_user)):
    address_service = AddressServices(db)
    address = address_service.update_address_info(data=data, user_id=current_user.id)
    return address


@address.get('/provinces', response_model=list[schemas.Province])
def get_all_province(db:Session=Depends(get_db)):
    address_service = AddressServices(db)
    provinces = address_service.get_all_province()
    return provinces



@address.get('/provinces/{province_id}/districts', response_model=list[schemas.District])
def get_district_by_province(province_id:int, db:Session=Depends(get_db)):
    address_service = AddressServices(db)
    districts = address_service.get_district_within_province(province_id=province_id)
    return districts


@address.get('/districts/{district_id}/municipalities', response_model=list[schemas.Municipality])
def get_municipalities_by_district(district_id:int, db:Session=Depends(get_db)):
    address_service = AddressServices(db)
    municipalities = address_service.get_municipality_within_district(district_id=district_id)
    return municipalities