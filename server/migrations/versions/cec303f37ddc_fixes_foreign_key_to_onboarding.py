"""fixes foreign key to onboarding

Revision ID: cec303f37ddc
Revises: 132964ce595a
Create Date: 2024-04-05 09:11:04.103329

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cec303f37ddc'
down_revision = '132964ce595a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('onboardings', sa.Column('employee_id', sa.Integer(), nullable=True))
    op.create_foreign_key(op.f('fk_onboardings_employee_id_employees'), 'onboardings', 'employees', ['employee_id'], ['id'])
    op.create_foreign_key(op.f('fk_reviews_employee_id_employees'), 'reviews', 'employees', ['employee_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('fk_reviews_employee_id_employees'), 'reviews', type_='foreignkey')
    op.drop_constraint(op.f('fk_onboardings_employee_id_employees'), 'onboardings', type_='foreignkey')
    op.drop_column('onboardings', 'employee_id')
    # ### end Alembic commands ###
