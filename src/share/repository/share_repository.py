import sqlalchemy as sa
from src.entrypoint.database import Base


class AbstractModel(Base):
    """Base Models

    Args:
        Base (_type_): Inherits Base from SQLAlchemy and specifies columns for inheritance.
    """

    __abstract__ = True

    id = sa.Column(sa.Integer, nullable=False, primary_key=True)
    
  

    pass


class ShareRepo(AbstractModel):
    __tablename__ = "share"
    Company = sa.Column(sa.VARCHAR)
    LTP = sa.Column(sa.VARCHAR)
    CHG = sa.Column(sa.VARCHAR)
    CHG_percent = sa.Column(sa.VARCHAR)
    HIGH = sa.Column(sa.VARCHAR)
    LOW = sa.Column(sa.VARCHAR)
    Open= sa.Column(sa.VARCHAR)
    Quantity = sa.Column(sa.VARCHAR)
    txn= sa.Column(sa.VARCHAR)
    
  
        

   
   
