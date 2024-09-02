"""0001_initial_migration

Revision ID: 7216cc08a545
Revises: 
Create Date: 2024-04-30 16:41:08.416351

"""
from typing import Sequence, Union

from alembic.op import create_table, drop_table
from sqlalchemy import Column, Integer, String, Boolean, ForeignKeyConstraint, PrimaryKeyConstraint
from sqlalchemy import sql

# revision identifiers, used by Alembic.
revision: str = '7216cc08a545'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    create_table(
        'shopUsers',
        Column('id', Integer, primary_key=True),
        Column('username', String(50), unique=True, nullable=False),
        Column('email', String(50), unique=True, nullable=False),
        Column('password', String(50), unique=False, nullable=False),
        Column('id', Integer, primary_key=True),
        Column('isAdmin', Boolean, unique=False, nullable=False, server_default=sql.expression.false()),
    )
    create_table(
        'shopProduct',
        Column('id', Integer, primary_key=True),
        Column('name', String(50), unique=True, nullable=False),
        Column('description', String, unique=False, nullable=False),
        Column('price', Integer, unique=False, nullable=False),
    )
    create_table(
        'busketShop',
        Column('idUser', Integer(), nullable=True),
        ForeignKeyConstraint(['idUser'], ['shopUsers.id'], ),
        PrimaryKeyConstraint('idUser')
    )


def downgrade() -> None:
    drop_table('shopUsers')
    drop_table('shopProduct')
    drop_table('busketShop')
