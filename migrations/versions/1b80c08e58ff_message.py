"""message

Revision ID: 1b80c08e58ff
Revises: 
Create Date: 2024-04-14 18:21:00.524142

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1b80c08e58ff'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sweets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('vendors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('vendor_sweets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('sweet_id', sa.Integer(), nullable=True),
    sa.Column('vendor_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['sweet_id'], ['sweets.id'], name=op.f('fk_vendor_sweets_sweet_id_sweets')),
    sa.ForeignKeyConstraint(['vendor_id'], ['vendors.id'], name=op.f('fk_vendor_sweets_vendor_id_vendors')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vendor_sweets')
    op.drop_table('vendors')
    op.drop_table('sweets')
    # ### end Alembic commands ###
