"""add foreign key to posts table

Revision ID: fae9d0731bc7
Revises: 00d54b51a133
Create Date: 2021-12-04 18:44:04.650578

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.util.compat import local_dataclass_fields


# revision identifiers, used by Alembic.
revision = 'fae9d0731bc7'
down_revision = '00d54b51a133'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("user_id", sa.Integer(), nullable=False))
    op.create_foreign_key("posts_users_fk", source_table="posts", referent_table="users", 
    local_cols=["user_id"], remote_cols=["id"], ondelete="CASCADE")


def downgrade():
    op.drop_constraint("posts_users_fk", "posts")
    op.drop_column("posts", "user_id")
