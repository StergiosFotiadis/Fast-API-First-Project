"""empty message

Revision ID: 3d67951fc2a6
Revises: f574a7a8c62e
Create Date: 2026-01-05 20:22:31.890889

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3d67951fc2a6'
down_revision: Union[str, Sequence[str], None] = 'f574a7a8c62e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
