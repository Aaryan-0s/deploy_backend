"""Connecting address table to master table

Revision ID: a3dbfd8cdc6b
Revises: d533b0daa148
Create Date: 2024-02-29 14:00:01.650221

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a3dbfd8cdc6b'
down_revision: Union[str, None] = 'd533b0daa148'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

# def upgrade() -> None:
#     op.create_table(
#         'address',
#         sa.Column('id', sa.Integer, primary_key=True, autoincrement=True, unique=True , index=True),
#         sa.Column('province', sa.VARCHAR(255), nullable=False),
#         sa.Column('district', sa.VARCHAR(255), nullable=False),
#         sa.Column('municipality', sa.VARCHAR(255), nullable=False),
#         sa.Column('ward', sa.Integer, nullable=False),
#         sa.Column('tole', sa.VARCHAR(255), nullable=False),
#         sa.Column('remarks', sa.VARCHAR(255)),
#         sa.Column('created_by', sa.String(225), server_default=sa.text("'SYSTEM'")),
#         sa.Column('created_on', sa.DateTime, server_default=sa.func.current_timestamp()),
#         sa.Column('modified_by', sa.VARCHAR(255)),
#         sa.Column('modified_on', sa.DateTime)
        # )

def upgrade() -> None:

    op.drop_column('address', column_name='province')
    op.drop_column('address', column_name='district')
    op.drop_column('address', column_name='municipality')
    op.drop_column('address', column_name='created_by')
    op.drop_column('address', column_name='modified_by')
    
    op.alter_column('address',column_name='ward',existing_type=sa.INTEGER,type_=sa.INTEGER ,nullable=True)
    op.alter_column('address',column_name='tole',existing_type=sa.VARCHAR(255),type_=sa.VARCHAR(255), nullable=True)
    
    op.add_column('address', sa.Column('municipality_id', sa.Integer, sa.ForeignKey('municipality.id'), nullable=False))
    


def downgrade():
    op.drop_column('address', column_name='municipality_id')

    op.alter_column('address', 'ward', nullable=False)
    op.alter_column('address', 'tole', nullable=False)

    op.add_column('address', sa.Column('province', sa.VARCHAR(255), nullable=False))
    op.add_column('address', sa.Column('district', sa.VARCHAR(255), nullable=False))
    op.add_column('address', sa.Column('municipality', sa.VARCHAR(255), nullable=False))
    op.add_column('address', sa.Column('created_by', sa.String(225), server_default=sa.text("'SYSTEM'")))
    op.add_column('address', sa.Column('modified_by', sa.VARCHAR(225)))