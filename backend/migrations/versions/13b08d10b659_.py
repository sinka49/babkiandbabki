"""empty message

Revision ID: 13b08d10b659
Revises: 74d948a821da
Create Date: 2023-05-20 21:52:15.208701

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '13b08d10b659'
down_revision = '74d948a821da'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('drink_ingridients', sa.Column('drink_id', postgresql.UUID(as_uuid=True), nullable=True))
    op.add_column('drink_ingridients', sa.Column('ingridient_id', postgresql.UUID(as_uuid=True), nullable=True))
    op.create_foreign_key(None, 'drink_ingridients', 'ingridients', ['ingridient_id'], ['ID'])
    op.create_foreign_key(None, 'drink_ingridients', 'drinks', ['drink_id'], ['ID'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'drink_ingridients', type_='foreignkey')
    op.drop_constraint(None, 'drink_ingridients', type_='foreignkey')
    op.drop_column('drink_ingridients', 'ingridient_id')
    op.drop_column('drink_ingridients', 'drink_id')
    # ### end Alembic commands ###