from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

myapp_obj = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

myapp_obj.config.update(
    SECRET_KEY='this-is-a-secret',
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db'),
    SQLALCHEMY_TRACK_MODIFICATIONS = False
)
db = SQLAlchemy(myapp_obj)
migrate = Migrate(myapp_obj, db)
with myapp_obj.app_context():
    db.create_all()
login = LoginManager(myapp_obj)

login.login_view = 'login'

UPLOAD_FOLDER = 'static/images/'
myapp_obj.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

from app import routes, models



