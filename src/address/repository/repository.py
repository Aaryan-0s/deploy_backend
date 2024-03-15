
from sqlalchemy import func
from sqlalchemy.orm import Session


from src.address.model.models import Province, District, Municipality, Address
from src.address.schema import schemas


class AddressRepo():
    
    def __init__(self, db:Session):
        self.db = db
        
    
    def fetch_all_province(self):
        return self.db.query(Province).all()

    def fetch_province_by_id(self, id:int):
        return self.db.query(Province).filter(Province.id == id).first()
    
    def fetch_province_by_name(self, name : str):
        return self.db.query(Province).filter(func.lower(Province.name) == func.lower(name)).first()
    
    
    
    def fetch_all_districts(self):
        return  self.db.query(District).all()

    def fetch_district_by_id(self, id: int):
        return self.db.query(District).filter(District.id == id).first()
    
    def fetch_district_by_name(self, name : str):
        return self.db.query(District).filter(func.lower(District.name) == func.lower(name)).first()
    
    def fetch_all_district_within_province(self, province_id : int):
        return self.db.query(District).filter(District.province_id == province_id).all()
    
    
    
    
    def fetch_all_municipalities(self):
        return self.db.query(Municipality).all()

    def fetch_municipality_by_id(self, id: int):
        return self.db.query(Municipality).filter(Municipality.id == id).first()
    
    def fetch_municipality_by_name(self, name : str):
        return self.db.query(Municipality).filter(func.lower(Municipality.name) == func.lower(name)).first()
    
    def fetch_all_municipality_within_district(self, district_id:int):
        return self.db.query(Municipality).filter(Municipality.district_id == district_id).all()
    

        
    
    
    def fetch_address_by_id(self, id:int):
        return self.db.query(Address).filter(Address.id == id).first()
    
    
    def add_new_address(self, data : schemas.AddressCreate):
        new_address = Address(**data.model_dump())
        self.db.add(new_address)
        self.db.commit()
        self.db.refresh(new_address)
        return new_address
    
    
    def update_address(self, new_data:schemas.AddressUpdate):
        self.db.commit()
        self.db.refresh(new_data)
        return new_data