from . import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    entries = db.relationship('Entry', backref='user', lazy=True)


class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_input = db.Column(db.String(200), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
