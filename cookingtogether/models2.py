"""Models for Cooking app."""

# import ipdb; ipdb.set_trace()

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class Post(db.Model):
    """Post"""
    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    hid = db.Column(db.Integer, db.ForeignKey('post_hid.id'))
    hash = db.Column(db.Text)

    title = db.Column(db.Text)
    summary = db.Column(db.Text)
    content = db.Column(db.Text)

    post_type_id = db.Column(db.Integer, db.ForeignKey('any_value.id'))

    created_date = db.Column(db.DateTime)
    author_id = db.Column(db.Integer, db.ForeignKey('entity.id'))
    modified_date = db.Column(db.DateTime)
    editor_id = db.Column(db.Integer, db.ForeignKey('entity.id'))

    sent_date = db.Column(db.DateTime)
    sender_id = db.Column(db.Integer, db.ForeignKey('entity.id'))
    read_date = db.Column(db.DateTime)
    receiver_id = db.Column(db.Integer, db.ForeignKey('entity.id'))

    is_enabled = db.Column(db.Boolean, default=True)
    is_deleted = db.Column(db.Boolean, default=False)

    table_id = db.Column(db.Integer, db.ForeignKey('entity.id'))
    row_id = db.Column(db.Integer)

    reply_to_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    reply_to_hid = db.Column(db.Integer, db.ForeignKey('post_hid.id'))

    def __repr__(s) -> str:
        return f"<{s.__tablename__} {s.id} {s.hid} {s.hash} {s.title} {s.author_id} {s.created_date}>"


class Post_Hid(db.Model):
    """Post_Hid"""
    __tablename__ = 'post_hid'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    hash = db.Column(db.Text)

    title = db.Column(db.Text)
    summary = db.Column(db.Text)
    content = db.Column(db.Text)

    post_type_id = db.Column(db.Integer, db.ForeignKey('any_value.id'))

    created_date = db.Column(db.DateTime)
    author_id = db.Column(db.Integer, db.ForeignKey('entity.id'))
    modified_date = db.Column(db.DateTime)
    editor_id = db.Column(db.Integer, db.ForeignKey('entity.id'))

    sent_date = db.Column(db.DateTime)
    sender_id = db.Column(db.Integer, db.ForeignKey('entity.id'))
    read_date = db.Column(db.DateTime)
    receiver_id = db.Column(db.Integer, db.ForeignKey('entity.id'))

    is_enabled = db.Column(db.Boolean, default=True)
    is_deleted = db.Column(db.Boolean, default=False)

    table_id = db.Column(db.Integer, db.ForeignKey('entity.id'))
    row_id = db.Column(db.Integer)

    reply_to_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    reply_to_hid = db.Column(db.Integer, db.ForeignKey('post_hid.id'))

    def __repr__(s) -> str:
        return f"<{s.__tablename__} {s.id} {s.post_id} {s.hash} {s.title} {s.author_id} {s.created_date}>"
