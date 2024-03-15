"""Add created_on and expiration_date to verification_codes

Revision ID: 6fe700124d62
Revises: d83169a0dd31
Create Date: 2024-02-26 16:48:58.832060

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6fe700124d62'
down_revision: Union[str, None] = 'd83169a0dd31'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    
    op.add_column('verification_codes', sa.Column('created_on', sa.DateTime, server_default=sa.func.now()))
    op.add_column('verification_codes', sa.Column('expiration_date', sa.DateTime, nullable=False, default=sa.func.now()))
    
    pass


def downgrade() -> None:
    pass
