"""create freebies table

Revision ID: db3651352972
Revises: 5f72c58bf48c
Create Date: 2025-06-05 11:47:22.155610

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'db3651352972'
down_revision = '5f72c58bf48c'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "freebies",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("item_name", sa.String, nullable=False),
        sa.Column("value", sa.Integer, nullable=False, default=0),
        sa.Column("dev_id", sa.Integer, sa.ForeignKey("devs.id"), nullable=False),
        sa.Column("company_id", sa.Integer, sa.ForeignKey("companies.id"), nullable=False),
        sa.CheckConstraint("value >= 0", name="check_value_non_negative")
    )


def downgrade():
    op.drop_table("freebies")