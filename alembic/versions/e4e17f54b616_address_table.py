"""address table

Revision ID: e4e17f54b616
Revises: 
Create Date: 2024-02-21 20:24:47.152700

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e4e17f54b616'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None




def upgrade() -> None:
    op.create_table(
        'address',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True, unique=True , index=True),
        sa.Column('province', sa.VARCHAR(255), nullable=False),
        sa.Column('district', sa.VARCHAR(255), nullable=False),
        sa.Column('municipality', sa.VARCHAR(255), nullable=False),
        sa.Column('ward', sa.Integer, nullable=False),
        sa.Column('tole', sa.VARCHAR(255), nullable=False),
        sa.Column('remarks', sa.VARCHAR(255)),
        sa.Column('created_by', sa.String(225), server_default=sa.text("'SYSTEM'")),
        sa.Column('created_on', sa.DateTime, server_default=sa.func.current_timestamp()),
        sa.Column('modified_by', sa.VARCHAR(255)),
        sa.Column('modified_on', sa.DateTime)
        )


def downgrade() -> None:
    op.drop_table('address')