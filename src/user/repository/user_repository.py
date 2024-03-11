import sqlalchemy as sa
from src.entrypoint.database import Base


class AbstractModel(Base):
    """Base Models

    Args:
        Base (_type_): Inherits Base from SQLAlchemy and specifies columns for inheritance.
    """

    __abstract__ = True

    id = sa.Column(sa.Integer, nullable=False, primary_key=True)
    date_created = sa.Column(
        sa.TIMESTAMP(timezone=True), server_default=sa.text("NOW()")
    )
    date_updated = sa.Column(
        sa.TIMESTAMP(timezone=True), server_default=sa.text("NOW()")
    )
  

    pass


class UserRepo(AbstractModel):
    __tablename__ = "user"
    username = sa.Column(sa.VARCHAR)
    password = sa.Column(sa.VARCHAR)
    email = sa.Column(sa.VARCHAR)
    
  
        

   
   
