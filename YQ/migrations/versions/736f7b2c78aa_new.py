"""new

Revision ID: 736f7b2c78aa
Revises: 
Create Date: 2019-11-15 00:22:58.517784

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '736f7b2c78aa'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('review',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('reviewID', sa.Integer(), nullable=False),
    sa.Column('overall', sa.Integer(), nullable=True),
    sa.Column('reviewText', sa.String(length=128), nullable=True),
    sa.Column('summary', sa.String(length=64), nullable=True),
    sa.Column('unixReviewTime', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id', 'reviewID')
    )
    op.create_index(op.f('ix_review_overall'), 'review', ['overall'], unique=False)
    op.create_index(op.f('ix_review_reviewText'), 'review', ['reviewText'], unique=False)
    op.create_index(op.f('ix_review_summary'), 'review', ['summary'], unique=False)
    op.create_index(op.f('ix_review_unixReviewTime'), 'review', ['unixReviewTime'], unique=False)
    op.create_table('reviewer_information',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('reviewerID', sa.String(length=64), nullable=False),
    sa.Column('reviewerName', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id', 'reviewerID')
    )
    op.create_index(op.f('ix_reviewer_information_reviewerName'), 'reviewer_information', ['reviewerName'], unique=False)
    op.create_table('reviewer_reviews',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('reviewID', sa.Integer(), nullable=False),
    sa.Column('asin', sa.String(length=64), nullable=True),
    sa.Column('reviewerID', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id', 'reviewID')
    )
    op.create_index(op.f('ix_reviewer_reviews_asin'), 'reviewer_reviews', ['asin'], unique=False)
    op.create_table('trial',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('reviewID', sa.Integer(), nullable=False),
    sa.Column('asin', sa.String(length=64), nullable=True),
    sa.Column('overall', sa.Integer(), nullable=True),
    sa.Column('reviewText', sa.String(length=128), nullable=True),
    sa.Column('reviewTime', sa.String(length=128), nullable=True),
    sa.Column('reviewerID', sa.String(length=64), nullable=True),
    sa.Column('reviewerName', sa.String(length=64), nullable=True),
    sa.Column('summary', sa.String(length=64), nullable=True),
    sa.Column('unixReviewTime', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id', 'reviewID')
    )
    op.create_index(op.f('ix_trial_asin'), 'trial', ['asin'], unique=False)
    op.create_index(op.f('ix_trial_overall'), 'trial', ['overall'], unique=False)
    op.create_index(op.f('ix_trial_reviewText'), 'trial', ['reviewText'], unique=False)
    op.create_index(op.f('ix_trial_reviewTime'), 'trial', ['reviewTime'], unique=False)
    op.create_index(op.f('ix_trial_reviewerID'), 'trial', ['reviewerID'], unique=False)
    op.create_index(op.f('ix_trial_reviewerName'), 'trial', ['reviewerName'], unique=False)
    op.create_index(op.f('ix_trial_summary'), 'trial', ['summary'], unique=False)
    op.create_index(op.f('ix_trial_unixReviewTime'), 'trial', ['unixReviewTime'], unique=False)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_bash', sa.String(length=128), nullable=True),
    sa.Column('about_me', sa.String(length=140), nullable=True),
    sa.Column('last_seen', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(length=140), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_post_timestamp'), 'post', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_post_timestamp'), table_name='post')
    op.drop_table('post')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_trial_unixReviewTime'), table_name='trial')
    op.drop_index(op.f('ix_trial_summary'), table_name='trial')
    op.drop_index(op.f('ix_trial_reviewerName'), table_name='trial')
    op.drop_index(op.f('ix_trial_reviewerID'), table_name='trial')
    op.drop_index(op.f('ix_trial_reviewTime'), table_name='trial')
    op.drop_index(op.f('ix_trial_reviewText'), table_name='trial')
    op.drop_index(op.f('ix_trial_overall'), table_name='trial')
    op.drop_index(op.f('ix_trial_asin'), table_name='trial')
    op.drop_table('trial')
    op.drop_index(op.f('ix_reviewer_reviews_asin'), table_name='reviewer_reviews')
    op.drop_table('reviewer_reviews')
    op.drop_index(op.f('ix_reviewer_information_reviewerName'), table_name='reviewer_information')
    op.drop_table('reviewer_information')
    op.drop_index(op.f('ix_review_unixReviewTime'), table_name='review')
    op.drop_index(op.f('ix_review_summary'), table_name='review')
    op.drop_index(op.f('ix_review_reviewText'), table_name='review')
    op.drop_index(op.f('ix_review_overall'), table_name='review')
    op.drop_table('review')
    # ### end Alembic commands ###