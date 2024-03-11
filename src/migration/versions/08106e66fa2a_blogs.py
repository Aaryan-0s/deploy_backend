"""blogs

Revision ID: 08106e66fa2a
Revises: 33ecfa852d27
Create Date: 2024-02-05 16:18:34.187912

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '08106e66fa2a'
down_revision: Union[str, None] = '33ecfa852d27'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "blogs",
        sa.Column("id", sa.Integer,primary_key=True,nullable=False),
        sa.Column("title", sa.VARCHAR(64), nullable=False),
        sa.Column("content", sa.TEXT, nullable=False),
        sa.Column("author", sa.VARCHAR(32), nullable=False),
        sa.Column("publication_date", sa.DATE, nullable=False),
        sa.Column("tags", sa.JSON, nullable=False),
        sa.Column(
            "date_created", sa.TIMESTAMP(timezone=True), server_default=sa.text("now()")
        ),
        sa.Column(
            "date_updated", sa.TIMESTAMP(timezone=True), server_default=sa.text("now()")
        ),
      
    )
    pass
    


def downgrade() -> None:
    op.drop_table("blogs")
    pass
