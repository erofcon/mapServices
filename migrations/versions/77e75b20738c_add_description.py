"""add description

Revision ID: 77e75b20738c
Revises: f755d2b6c738
Create Date: 2023-09-09 15:52:07.119914

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '77e75b20738c'
down_revision = 'f755d2b6c738'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('route', sa.Column('description', sa.String(), nullable=True))
    op.add_column('transport', sa.Column('description', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('transport', 'description')
    op.drop_column('route', 'description')
    # ### end Alembic commands ###