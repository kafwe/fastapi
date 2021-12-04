"""add content column to posts table

Revision ID: 63361c4fb403
Revises: ef6574ef1d1b
Create Date: 2021-12-04 18:29:59.365329

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '63361c4fb403'
down_revision = 'ef6574ef1d1b'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))


def downgrade():
    op.drop_column("posts", "content")
