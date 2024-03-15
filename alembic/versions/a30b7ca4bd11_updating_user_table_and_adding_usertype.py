"""updating user table and adding usertype

Revision ID: a30b7ca4bd11
Revises: 0fb6a0d8285c
Create Date: 2024-03-12 13:29:48.915948

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a30b7ca4bd11'
down_revision: Union[str, None] = '0fb6a0d8285c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('usertype', sa.String(255), nullable=False, default='user'))
    pass


def downgrade() -> None:
    pass
