"""第九次提交

Revision ID: 7dc55bc91f6e
Revises: 8f6aca1c1c8f
Create Date: 2022-01-15 22:40:38.550800

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '7dc55bc91f6e'
down_revision = '8f6aca1c1c8f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('t_rolemenu', 'role_id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
    op.alter_column('t_rolemenu', 'menu_id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('t_rolemenu', 'menu_id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('t_rolemenu', 'role_id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    # ### end Alembic commands ###
