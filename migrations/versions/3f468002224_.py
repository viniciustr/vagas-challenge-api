"""empty message

Revision ID: 3f468002224
Revises: 51e2c29ad95
Create Date: 2019-01-13 17:50:58.203209

"""

# revision identifiers, used by Alembic.
revision = '3f468002224'
down_revision = '51e2c29ad95'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pessoas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=300), nullable=False),
    sa.Column('profissao', sa.String(length=300), nullable=False),
    sa.Column('localizacao', sa.String(length=300), nullable=False),
    sa.Column('nivel', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pessoas')
    ### end Alembic commands ###