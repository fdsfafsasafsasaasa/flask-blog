from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

app.secret_key = "pakt"

db = SQLAlchemy(app)

login_manager = LoginManager(app)

from pakt_blog import routes