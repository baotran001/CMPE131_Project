from app import db
from werkzeug.security import generate_password_hash, check_password_hash

from app import login
from flask_login import UserMixin

from flask import url_for
from sqlalchemy.sql import func

from datetime import datetime

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String(200))
    email = db.Column(db.String(32), unique=True)
    #image_file = db.Column(db.String(20), nullable=False, default="default.jpg")
    posts = db.relationship('Post', backref='author', lazy=True)
  

    followers = db.Table('followers', 
                db.Column('follower_id', db.Integer, db.ForeignKey('user.id')), 
                db.Column('followed_id', db.Integer, db.ForeignKey('user.id')))

    followed = db.relationship('User', secondary=followers, 
                                primaryjoin=(followers.c.follower_id == id), 
                                secondaryjoin=(followers.c.followed_id == id),
                                backref=db.backref('followers', lazy='dynamic'), lazy='dynamic')

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def get_password(self):
        return self.password
    
    def set_picture(self, profile_pic):
        self.profile_pic = profile_pic
        
    def set_username(self, username):
        self.username = username

    def __repr__(self):
        return f'<User {self.username}>'

    def follow(self, user):
        if not self.is_following(user):
            self.followed.append(user)

    def unfollow(self, user):
        if self.is_following(user):
            self.followed.remove(user)

#    def is_following(self, user):
#        return self.followed.filter(followers.c.followed_id == user.id).count() > 0

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class Post(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)