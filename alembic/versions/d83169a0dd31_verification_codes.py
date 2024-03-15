"""verification codes

Revision ID: d83169a0dd31
Revises: 56da41e91d0d
Create Date: 2024-02-23 15:07:27.081518

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd83169a0dd31'
down_revision: Union[str, None] = '56da41e91d0d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'verification_codes',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True, unique=True),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id'), unique=True, nullable=False, index=True),
        sa.Column('code', sa.Integer, nullable=False)
    )
    pass


def downgrade() -> None:
    pass
