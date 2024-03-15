import sqlalchemy as sa
from sqlalchemy.orm import relationship

from src.entrypoint.database import Base


class User(Base):
    __tablename__ = "users"
    
    
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True, unique=True , index=True)
    username = sa.Column(sa.VARCHAR(255), nullable=False)
    hashed_password = sa.Column(sa.VARCHAR(255), nullable=False)
    email = sa.Column(sa.VARCHAR(255), nullable=False, index=True)
    first_name = sa.Column(sa.VARCHAR(255))
    last_name = sa.Column(sa.VARCHAR(255))
    is_active = sa.Column(sa.Boolean, default=True)
    is_verified = sa.Column(sa.Boolean, default=False)
    address_id = sa.Column(sa.Integer, sa.ForeignKey('address.id'))
    created_by = sa.Column(sa.String(225), server_default=sa.text("'SYSTEM'"))
    created_on = sa.Column(sa.DateTime, server_default=sa.func.current_timestamp())
    usertype = sa.Column(sa.String(255), default=sa.text("'USER'"))



    
    

class VerificationCode(Base): 
    __tablename__ = "verification_codes"
    
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True, unique=True)
    user_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'), unique=True, nullable=False, index=True)
    code = sa.Column(sa.Integer, nullable=False)
    created_on = sa.Column(sa.DateTime, server_default=sa.func.now())
    expiration_date = sa.Column(sa.DateTime)
    
    