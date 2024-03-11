"""crud

Revision ID: 33ecfa852d27
Revises: 
Create Date: 2024-02-05 13:21:21.780829

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '33ecfa852d27'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "crud",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("username",sa.VARCHAR(55),nullable=False),
        sa.Column("firstname",sa.VARCHAR(255),nullable=False),
        sa.Column("lastname",sa.VARCHAR(255),nullable=False),
        sa.Column("dob",sa.Date,nullable=False),
        sa.Column("gender",sa.VARCHAR(255),nullable=False),
        sa.Column("email",sa.VARCHAR(255),nullable=False),
      )
    
    pass


def downgrade() -> None:
    op.drop_table("crud")
    pass
