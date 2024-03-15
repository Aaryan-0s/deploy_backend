"""Master tables for address

Revision ID: d533b0daa148
Revises: 6fe700124d62
Create Date: 2024-02-29 13:57:47.571481

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd533b0daa148'
down_revision: Union[str, None] = '6fe700124d62'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "province",
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True, unique=True),
        sa.Column('name', sa.VARCHAR(255), unique=True, index=True, nullable=False ),
        sa.Column('created_by', sa.String(225), server_default=sa.text("'SYSTEM'")),
        sa.Column('created_on', sa.DateTime, server_default=sa.func.current_timestamp()),
    )
    
    op.create_table(
        'district',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True, unique=True),
        sa.Column('name', sa.VARCHAR(255), unique=True, index=True, nullable=False ),
        sa.Column('province_id', sa.Integer, sa.ForeignKey('province.id'), nullable=False),
        sa.Column('created_by', sa.String(225), server_default=sa.text("'SYSTEM'")),
        sa.Column('created_on', sa.DateTime, server_default=sa.func.current_timestamp()),
    )
    op.create_table(
        'municipality',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True, unique=True),
        sa.Column('name', sa.VARCHAR(255), index=True, nullable=False ),
        sa.Column('num_of_ward', sa.Integer),
        sa.Column('district_id', sa.Integer, sa.ForeignKey('district.id'), nullable=False),
        sa.Column('created_by', sa.String(225), server_default=sa.text("'SYSTEM'")),
        sa.Column('created_on', sa.DateTime, server_default=sa.func.current_timestamp()),
    )
    pass


def downgrade() -> None:
    op.drop_table('province')
    op.drop_table('district')
    op.drop_table('municipality')
    pass