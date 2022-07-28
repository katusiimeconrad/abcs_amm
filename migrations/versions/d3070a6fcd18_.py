"""empty message

Revision ID: d3070a6fcd18
Revises: a8efa99a3bdb
Create Date: 2021-12-20 21:52:19.292847

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd3070a6fcd18'
down_revision = 'a8efa99a3bdb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product', sa.Column('price', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('product', 'price')
    # ### end Alembic commands ###
