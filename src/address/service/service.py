from fastapi import HTTPException, status
from sqlalchemy.orm import Session


from src.address.schema import schemas
from src.address.repository.repository import AddressRepo
from src.user.service.services import UserServices


class AddressServices():
    
    def __init__(self, db:Session):
        self.repo = AddressRepo(db)
        self.user_service = UserServices(db)
        
        
    def get_all_province(self):
        return self.repo.fetch_all_province()
    
    def get_district_within_province(self, province_id:int):
        districts =  self.repo.fetch_all_district_within_province(province_id=province_id)
        if districts is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid Province_id.")
        return districts
    
    def get_municipality_within_district(self, district_id:int):
        municipality = self.repo.fetch_all_municipality_within_district(district_id=district_id)
        if municipality is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid district_id.")
        return municipality
    
    def get_municipality_by_id(self, id:int):
        municipality = self.repo.fetch_municipality_by_id(id=id)
        if municipality is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid municipality_id.")
        return municipality
    
    
    def get_province_and_district_by_municipality_id(self, muni_id:int):
        municipality = self.get_municipality_by_id(muni_id)
        district = self.repo.fetch_district_by_id(municipality.district_id)
        province = self.repo.fetch_province_by_id(district.province_id)
        
        municipality_name = municipality.name
        district_name = district.name
        province_name = province.name
        
        return municipality_name, district_name, province_name
        
    
    def _get_address_by_id(self, id:int):
        address = self.repo.fetch_address_by_id(id=id)
        return address
    
    
    
    
    
    def get_user_address(self,user_id):
        user = self.user_service.get_user_by_id(user_id=user_id)
        if user.address_id is None:
            raise HTTPException(
                status_code = status.HTTP_400_BAD_REQUEST,
                detail = "Doesn't have address"
            )
        address = self._get_address_by_id(id=user.address_id)
        municipality_name, district_name, province_name =  self.get_province_and_district_by_municipality_id(muni_id=address.municipality_id)
        resp = schemas.UserAddress(
            municipality_name=municipality_name, 
            province_name=province_name, 
            district_name=district_name,
            ward=address.ward,
            tole=address.tole,
        )
        return resp
    
    
    def validate_address_info(self, data):
        municipality = self.get_municipality_by_id(data.municipality_id)
        if data.ward is not None and data.ward > municipality.num_of_ward:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Ward no should be within 0-{municipality.num_of_ward}.")
        return True
    
    
    
    def add_address(self, data:schemas.AddressCreate, user_id:int):
        
        user = self.user_service.get_user_by_id(user_id=user_id)
        if user.address_id is not None:
            print("user address id is not none")
            address_update_data = schemas.AddressUpdate(**data.model_dump())
            address = self.update_address_info(data=address_update_data, user_id=user_id)
            return address
        
        if self.validate_address_info(data=data):
            user_address =  self.repo.add_new_address(data=data)
            print(user_address.id)
            # user_data = schemas.UserUpdate(address_id=user_address.id)
            user_data = self.user_service.save_address_id(address_id=user_address.id, user_id=user_id)
            # user = self.user_service.user_update(user_data=user_data, userid=str(user_id))
            
            return user_address
        
        
    
    
    def update_address_info(self, data:schemas.AddressUpdate, user_id:int):
        user = self.user_service.get_user_by_id(user_id=user_id)
        
        if user.address_id is None:
            address_create_data = schemas.AddressCreate(**data.model_dump())
            self.add_address(self, data=address_create_data, current_user=user)
        
        if self.validate_address_info(data=data):
            address = self.repo.fetch_address_by_id(user.address_id)
            update_data = data.model_dump(exclude_unset=True)
            
            for (k,v) in update_data.items():
                setattr(address, k, v)
            
            return self.repo.update_address(address)
    
   
        