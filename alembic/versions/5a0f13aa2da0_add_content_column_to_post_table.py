"""add content column to post table

Revision ID: 5a0f13aa2da0
Revises: 4bf856ef19da
Create Date: 2026-01-03 18:50:02.558169

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5a0f13aa2da0'
down_revision: Union[str, Sequence[str], None] = '4bf856ef19da'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', 'content')
    pass