"""create posts table

Revision ID: ef6574ef1d1b
Revises: 
Create Date: 2021-12-04 18:11:08.068406

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ef6574ef1d1b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("posts", sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
    sa.Column("title", sa.String(), nullable=False))


def downgrade():
    op.drop_table("posts")
