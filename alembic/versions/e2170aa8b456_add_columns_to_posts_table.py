"""add columns to posts table

Revision ID: e2170aa8b456
Revises: fae9d0731bc7
Create Date: 2021-12-04 18:53:00.724719

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e2170aa8b456'
down_revision = 'fae9d0731bc7'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column(
        "published", sa.Boolean(), nullable=False, server_default="TRUE"))
    op.add_column("posts", sa.Column(
        "created_at", sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text("NOW()")))


def downgrade():
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
