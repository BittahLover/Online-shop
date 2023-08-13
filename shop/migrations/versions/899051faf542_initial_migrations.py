"""initial migrations

Revision ID: 899051faf542
Revises: 
Create Date: 2022-06-27 04:48:24.753287

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '899051faf542'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('customer_order')
    op.add_column('register', sa.Column('f_name', sa.String(length=50), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('register', 'f_name')
    op.create_table('customer_order',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('invoice', sa.VARCHAR(length=20), nullable=False),
    sa.Column('status', sa.VARCHAR(length=20), nullable=False),
    sa.Column('customer_id', sa.INTEGER(), nullable=False),
    sa.Column('date_created', sa.DATETIME(), nullable=False),
    sa.Column('orders', sa.TEXT(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('invoice')
    )
    # ### end Alembic commands ###
