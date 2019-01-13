"""empty message

Revision ID: 35f92a4f83e
Revises: 3f468002224
Create Date: 2019-01-13 19:07:33.915318

"""

# revision identifiers, used by Alembic.
revision = '35f92a4f83e'
down_revision = '3f468002224'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vagas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('empresa', sa.String(length=300), nullable=False),
    sa.Column('titulo', sa.String(length=300), nullable=False),
    sa.Column('descricao', sa.String(length=1000), nullable=False),
    sa.Column('localizacao', sa.String(length=300), nullable=False),
    sa.Column('nivel', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vagas')
    ### end Alembic commands ###
