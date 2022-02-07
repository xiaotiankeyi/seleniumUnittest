"""1/21提交

Revision ID: 5def72558a53
Revises: 838f25233543
Create Date: 2022-01-21 23:18:31.983200

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5def72558a53'
down_revision = '838f25233543'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('t_goodsify',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=32), nullable=False),
    sa.Column('level', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('t_goodslist',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=32), nullable=False),
    sa.Column('level', sa.Integer(), nullable=True),
    sa.Column('goodsify_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['goodsify_id'], ['t_goodsify.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('t_goods',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=32), nullable=False),
    sa.Column('level', sa.Integer(), nullable=True),
    sa.Column('goodlist_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['goodlist_id'], ['t_goodslist.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('t_goods')
    op.drop_table('t_goodslist')
    op.drop_table('t_goodsify')
    # ### end Alembic commands ###
