"""create post table

Revision ID: 4bf856ef19da
Revises: 
Create Date: 2026-01-03 18:24:58.944905

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4bf856ef19da'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
    sa.Column('title', sa.String(), nullable=False),
    # sa.Column('content', sa.String(), nullable=False),
    # sa.Column('published', sa.Boolean(), nullable=False),
    # sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False),
    # sa.PrimaryKeyConstraint('id')
    )
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('posts')
    pass
