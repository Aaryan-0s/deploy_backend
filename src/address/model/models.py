import sqlalchemy as sa
from sqlalchemy.orm import relationship

from src.entrypoint.database import Base



class Address(Base):
    __tablename__ = "address"
    
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True, unique=True , index=True)
    municipality_id = sa.Column(sa.Integer)
    ward = sa.Column(sa.Integer)
    tole = sa.Column(sa.VARCHAR(255))
    remarks = sa.Column(sa.VARCHAR(255))
    created_on = sa.Column(sa.DateTime, server_default=sa.func.current_timestamp())
    modified_on = sa.Column(sa.DateTime)

    
    
class Province(Base):
    __tablename__ = "province"
 
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True, unique=True)
    name = sa.Column(sa.VARCHAR(255), unique=True, index=True, nullable=False )
    created_by = sa.Column(sa.String(225), server_default=sa.text("'SYSTEM'"))
    created_on = sa.Column(sa.DateTime, server_default=sa.func.current_timestamp())
    

        
class District(Base):
    __tablename__ = "district"
    
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True, unique=True)
    name = sa.Column(sa.VARCHAR(255), unique=True, index=True, nullable=False )
    province_id = sa.Column(sa.Integer, sa.ForeignKey('province.id'), nullable=False)
    created_by = sa.Column(sa.String(225), server_default=sa.text("'SYSTEM'"))
    created_on = sa.Column(sa.DateTime, server_default=sa.func.current_timestamp())
    


class Municipality(Base):
    __tablename__ = 'municipality'
    
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True, unique=True)
    name = sa.Column(sa.VARCHAR(255), unique=True, index=True, nullable=False )
    num_of_ward = sa.Column(sa.Integer)
    district_id = sa.Column(sa.Integer, sa.ForeignKey('district.id'), nullable=False)
    created_by = sa.Column(sa.String(225), server_default=sa.text("'SYSTEM'"))
    created_on = sa.Column(sa.DateTime, server_default=sa.func.current_timestamp())
