"""update 01 comments

Revision ID: 3f8a2f87e4b6
Revises: 7a6b858b72db
Create Date: 2024-06-11 17:02:52.939621

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '3f8a2f87e4b6'
down_revision: Union[str, None] = '7a6b858b72db'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comments')
    op.add_column('cinemas', sa.Column('manager_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'cinemas', 'managers', ['manager_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'cinemas', type_='foreignkey')
    op.drop_column('cinemas', 'manager_id')
    op.create_table('comments',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('movie_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('user_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('text', mysql.TEXT(), nullable=True),
    sa.Column('parent_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['movie_id'], ['movies.id'], name='comments_ibfk_1', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['parent_id'], ['comments.id'], name='comments_ibfk_4', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='comments_ibfk_3', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
