"""added Hero Powers table

Revision ID: 6ce413b23b04
Revises: e046cc2e34ff
Create Date: 2025-06-15 16:35:34.278146

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6ce413b23b04'
down_revision = 'e046cc2e34ff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('hero_powers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('strength', sa.String(), nullable=True),
    sa.Column('hero_id', sa.Integer(), nullable=True),
    sa.Column('power_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['hero_id'], ['heroes.id'], name=op.f('fk_hero_powers_hero_id_heroes')),
    sa.ForeignKeyConstraint(['power_id'], ['powers.id'], name=op.f('fk_hero_powers_power_id_powers')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('hero_powers')
    # ### end Alembic commands ###
