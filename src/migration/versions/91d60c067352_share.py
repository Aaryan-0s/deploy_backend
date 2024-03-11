"""share

Revision ID: 91d60c067352
Revises: 6f0972fcc8c9
Create Date: 2024-02-13 20:13:22.552135

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '91d60c067352'
down_revision: Union[str, None] = '6f0972fcc8c9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "share",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("Company",sa.VARCHAR(55),nullable=False),
        sa.Column("LTP",sa.VARCHAR(255),nullable=False),
        sa.Column("CHG",sa.VARCHAR(255),nullable=False),
        sa.Column("CHG_percent",sa.VARCHAR(255),nullable=False),
        sa.Column("HIGH",sa.VARCHAR(255),nullable=False),
        sa.Column("LOW",sa.VARCHAR(255),nullable=False),
        sa.Column("Open",sa.VARCHAR(255),nullable=False),
        sa.Column("Quantity",sa.VARCHAR(255),nullable=False),
        sa.Column("txn",sa.VARCHAR(255),nullable=False),
        
        
    )
    pass


def downgrade() -> None:
    op.drop_table("share")
    pass
