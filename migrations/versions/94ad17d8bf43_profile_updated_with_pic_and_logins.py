"""Profile updated with pic and logins

Revision ID: 94ad17d8bf43
Revises: 44c6edc034ff
Create Date: 2018-09-04 15:58:25.818273

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '94ad17d8bf43'
down_revision = '44c6edc034ff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('bio', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('password_secure', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('profile_pic_path', sa.String(), nullable=True))
    op.drop_column('users', 'password_hash')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_hash', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_column('users', 'profile_pic_path')
    op.drop_column('users', 'password_secure')
    op.drop_column('users', 'bio')
    # ### end Alembic commands ###
