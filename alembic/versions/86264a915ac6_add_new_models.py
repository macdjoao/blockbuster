"""add new models

Revision ID: 86264a915ac6
Revises: 40a8aef1c3d4
Create Date: 2023-06-12 18:05:33.259520
"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = '86264a915ac6'
down_revision = '40a8aef1c3d4'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'customers',
        sa.Column('id', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('is_active', sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email'),
    )
    op.create_table(
        'movies',
        sa.Column('id', sa.String(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('available', sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('name'),
    )
    op.create_table(
        'rents',
        sa.Column('id', sa.String(), nullable=False),
        sa.Column('user', sa.String(), nullable=True),
        sa.Column('customer', sa.String(), nullable=True),
        sa.Column('movie', sa.String(), nullable=True),
        sa.Column(
            'rent_date',
            sa.DateTime(timezone=True),
            server_default=sa.text('now()'),
            nullable=True,
        ),
        sa.Column(
            'devolution_date', sa.DateTime(timezone=True), nullable=True
        ),
        sa.Column('finished', sa.Boolean(), nullable=True),
        sa.ForeignKeyConstraint(
            ['customer'],
            ['customers.id'],
        ),
        sa.ForeignKeyConstraint(
            ['movie'],
            ['movies.id'],
        ),
        sa.ForeignKeyConstraint(
            ['user'],
            ['users.id'],
        ),
        sa.PrimaryKeyConstraint('id'),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('rents')
    op.drop_table('movies')
    op.drop_table('customers')
    # ### end Alembic commands ###
