"""empty message

Revision ID: 4eccd720acd8
Revises: a9185728f94f
Create Date: 2024-05-10 09:03:58.865343

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4eccd720acd8'
down_revision: Union[str, None] = 'a9185728f94f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tasks', sa.Column('update_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tasks', 'update_at')
    # ### end Alembic commands ###