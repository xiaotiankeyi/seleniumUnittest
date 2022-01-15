"""第八次提交

Revision ID: 8f6aca1c1c8f
Revises: a18bfadad1ba
Create Date: 2022-01-15 19:09:15.774800

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8f6aca1c1c8f'
down_revision = 'a18bfadad1ba'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('t_rolemenu',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.Column('menu_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['menu_id'], ['t_meun.id'], ),
    sa.ForeignKeyConstraint(['role_id'], ['t_role.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('t_rolemenu')
    # ### end Alembic commands ###
