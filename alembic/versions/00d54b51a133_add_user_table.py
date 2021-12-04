"""add user table

Revision ID: 00d54b51a133
Revises: 63361c4fb403
Create Date: 2021-12-04 18:36:04.674492

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '00d54b51a133'
down_revision = '63361c4fb403'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("users", 
                    sa.Column("id", sa.Integer(), nullable=False),
                    sa.Column("email", sa.String(), nullable=False),
                    sa.Column("password", sa.String(), nullable=False),
                    sa.Column("created_at", sa.TIMESTAMP(timezone=True), 
                              server_default=sa.text("now()"), nullable=False),
                              sa.PrimaryKeyConstraint("id"),
                              sa.UniqueConstraint("email")
                    )

def downgrade():
    op.drop_table("users")