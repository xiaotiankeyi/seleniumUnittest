"""1/21提交

Revision ID: e3325a1f4627
Revises: 5def72558a53
Create Date: 2022-01-21 23:33:36.571200

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e3325a1f4627'
down_revision = '5def72558a53'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('name', table_name='t_goods')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('name', 't_goods', ['name'], unique=False)
    # ### end Alembic commands ###
