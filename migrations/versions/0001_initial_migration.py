"""0001_initial_migration

Revision ID: 7216cc08a545
Revises: 
Create Date: 2024-04-30 16:41:08.416351

"""
from typing import Sequence, Union

from alembic.op import create_table, drop_table
from sqlalchemy import Column, String


# revision identifiers, used by Alembic.
revision: str = '7216cc08a545'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    create_table(
        'shopUsers',
        Column('nameUser', String(50), nullable=False),
        Column('mailUser', String(50), nullable=False),
        Column('passwordUser', String(50), nullable=False),
    )


def downgrade() -> None:
    drop_table('shopUsers')
