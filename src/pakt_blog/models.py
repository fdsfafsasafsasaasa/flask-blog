from sqlalchemy.orm import backref, relationship
from pakt_blog import db, login_manager

from sqlalchemy.types import Integer, String

from flask_login import UserMixin

from werkzeug.security import generate_password_hash

@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(user_id)

class User(UserMixin, db.Model):

    id = db.Column(Integer, primary_key=True)

    name = db.Column(String)

    password = db.Column(String)

    authenticated = db.Column(db.Boolean, default=False)

    posts = relationship("Post", backref="user")

class Post(db.Model):

    id = db.Column(Integer, primary_key=True)

    name = db.Column(String)

    author = db.Column(String, db.ForeignKey('user.name'))

    body = db.Column(String)
