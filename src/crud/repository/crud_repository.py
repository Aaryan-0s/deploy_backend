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


class CrudRepo(AbstractModel):
    __tablename__ = "crud"
    username = sa.Column(sa.VARCHAR)
    firstname = sa.Column(sa.VARCHAR)
    lastname = sa.Column(sa.VARCHAR)
    dob = sa.Column(sa.Date)
    gender = sa.Column(sa.VARCHAR)
    email = sa.Column(sa.VARCHAR)

   
   
