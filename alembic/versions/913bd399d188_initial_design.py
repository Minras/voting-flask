"""initial design

Revision ID: 913bd399d188
Revises: 
Create Date: 2018-11-05 20:21:27.574855

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '913bd399d188'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'works',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('path', sa.String(1024), nullable=False),
        sa.Column('name', sa.String(256), nullable=False),
        sa.Column('description', sa.Unicode(10240), nullable=False),
    )

    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True)
    )

    op.create_table(
        'user_votes',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id'), nullable=False),
        sa.Column('work_id', sa.Integer, sa.ForeignKey('works.id'), nullable=False),
        sa.Column('vote', sa.Integer, nullable=False),
    )

    op.create_table(
        'current_votes',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id'), nullable=False),
        sa.Column('work_id', sa.Integer, sa.ForeignKey('works.id'), nullable=False),
    )


def downgrade():
    pass
