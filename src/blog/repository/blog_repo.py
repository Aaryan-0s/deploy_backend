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


class BlogRepo(AbstractModel):
    __tablename__ = "blogs"
    title = sa.Column(sa.VARCHAR)
    content = sa.Column(sa.VARCHAR)
    author = sa.Column(sa.VARCHAR)
    publication_date = sa.Column(sa.DATE)
    tags = sa.Column(sa.ARRAY(sa.VARCHAR))
    
