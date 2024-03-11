"""user

Revision ID: 6f0972fcc8c9
Revises: 08106e66fa2a
Create Date: 2024-02-08 18:21:57.537511

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6f0972fcc8c9'
down_revision: Union[str, None] = '08106e66fa2a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "user",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("username",sa.VARCHAR(55),nullable=False),
        sa.Column("password",sa.VARCHAR(255),nullable=False),
        sa.Column("email",sa.VARCHAR(255),nullable=False),
        sa.Column(
            "date_created", sa.TIMESTAMP(timezone=True), server_default=sa.text("now()")
        ),
        sa.Column(
            "date_updated", sa.TIMESTAMP(timezone=True), server_default=sa.text("now()")
        ),
    )
    pass


def downgrade() -> None:
    pass
