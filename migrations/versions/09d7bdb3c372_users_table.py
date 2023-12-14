"""users table

Revision ID: 09d7bdb3c372
Revises: 
Create Date: 2023-12-13 23:14:46.082801

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '09d7bdb3c372'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('case_db',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('model', sa.String(length=50), nullable=False),
    sa.Column('price', sa.Float(precision=2), nullable=True),
    sa.Column('type', sa.String(length=20), nullable=True),
    sa.Column('color', sa.String(length=20), nullable=True),
    sa.Column('side_panel', sa.String(length=25), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('model')
    )
    op.create_table('cpu_cooler_db',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('model', sa.String(length=50), nullable=False),
    sa.Column('price', sa.Float(precision=2), nullable=True),
    sa.Column('size', sa.Integer(), nullable=True),
    sa.Column('rpm', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('model')
    )
    op.create_table('cpu_db',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('model', sa.String(length=50), nullable=False),
    sa.Column('price', sa.Float(precision=2), nullable=True),
    sa.Column('clockSpeed', sa.Float(precision=1), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('model')
    )
    op.create_table('drive_db',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('model', sa.String(length=50), nullable=False),
    sa.Column('price', sa.Float(precision=2), nullable=True),
    sa.Column('capacity', sa.Integer(), nullable=True),
    sa.Column('drive_type', sa.String(length=10), nullable=True),
    sa.Column('interface', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('model')
    )
    op.create_table('fans_db',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('model', sa.String(length=50), nullable=False),
    sa.Column('price', sa.Float(precision=2), nullable=True),
    sa.Column('size', sa.Integer(), nullable=True),
    sa.Column('rpm', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('model')
    )
    op.create_table('gpu_db',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('model', sa.String(length=50), nullable=False),
    sa.Column('price', sa.Float(precision=2), nullable=True),
    sa.Column('mem', sa.Integer(), nullable=False),
    sa.Column('core_clock', sa.Integer(), nullable=False),
    sa.Column('gpu_len', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('model')
    )
    op.create_table('mobo_db',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('model', sa.String(length=50), nullable=False),
    sa.Column('price', sa.Float(precision=2), nullable=True),
    sa.Column('mem_slot', sa.Integer(), nullable=False),
    sa.Column('mem_speed', sa.Integer(), nullable=False),
    sa.Column('socket_type', sa.String(length=20), nullable=False),
    sa.Column('form_factor', sa.String(length=10), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('model')
    )
    op.create_table('psu_db',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('model', sa.String(length=50), nullable=False),
    sa.Column('price', sa.Float(precision=2), nullable=True),
    sa.Column('form_factor', sa.String(length=5), nullable=True),
    sa.Column('effi', sa.String(length=10), nullable=True),
    sa.Column('wattage', sa.Integer(), nullable=True),
    sa.Column('mod', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('model')
    )
    op.create_table('ram_db',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('model', sa.String(length=50), nullable=False),
    sa.Column('price', sa.Float(precision=2), nullable=True),
    sa.Column('speed', sa.String(length=20), nullable=True),
    sa.Column('modules', sa.String(length=20), nullable=True),
    sa.Column('cas_latency', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('model')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=16), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('image_pfp', sa.String(length=16), nullable=False),
    sa.Column('password', sa.String(length=60), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('ram_db')
    op.drop_table('psu_db')
    op.drop_table('mobo_db')
    op.drop_table('gpu_db')
    op.drop_table('fans_db')
    op.drop_table('drive_db')
    op.drop_table('cpu_db')
    op.drop_table('cpu_cooler_db')
    op.drop_table('case_db')
    # ### end Alembic commands ###
