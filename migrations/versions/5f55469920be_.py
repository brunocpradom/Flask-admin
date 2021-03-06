"""empty message

Revision ID: 5f55469920be
Revises: 73ff69eeb209
Create Date: 2021-04-13 15:55:40.467278

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '5f55469920be'
down_revision = '73ff69eeb209'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('access',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('data', sa.Date(), nullable=True),
    sa.Column('hora', sa.Integer(), nullable=True),
    sa.Column('access', sa.Integer(), nullable=True),
    sa.Column('pagina', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('access')
    # ### end Alembic commands ###
