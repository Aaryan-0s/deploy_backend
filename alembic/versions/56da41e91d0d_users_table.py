"""Users table

Revision ID: 56da41e91d0d
Revises: e4e17f54b616
Create Date: 2024-02-21 20:27:07.870406

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '56da41e91d0d'
down_revision: Union[str, None] = 'e4e17f54b616'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True, unique=True , index=True),
        sa.Column('username', sa.VARCHAR(255), nullable=False),
        sa.Column('hashed_password', sa.VARCHAR(255), nullable=False),
        sa.Column('email', sa.VARCHAR(255), nullable=False, index=True),
        sa.Column('first_name', sa.VARCHAR(255)),
        sa.Column('last_name', sa.VARCHAR(255)),
        sa.Column('is_active', sa.Boolean, default=True),
        sa.Column('is_verified', sa.Boolean, default=False),
        sa.Column('address_id', sa.Integer, sa.ForeignKey('address.id')),
        sa.Column('created_by', sa.String(225), server_default=sa.text("'SYSTEM'")),
        sa.Column('created_on', sa.DateTime, server_default=sa.func.current_timestamp()),
        )
    pass

def downgrade() -> None:
    op.drop_table('users')
    pass