"""create books table

Revision ID: 1000
Revises: 
Create Date: 2024-08-01 13:51:51.224006

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1000'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Create the books table
    op.create_table(
        'books',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String(255), nullable=False),
        sa.Column('price', sa.String(50), nullable=False),
        sa.Column('availability', sa.String(100), nullable=False),

        
    )

def downgrade() -> None:
    # Drop the books table
    op.drop_table('books')

