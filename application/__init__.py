from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.bcrypt import Bcrypt


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../snap.db'
app.config['SECRET_KEY'] = '_-_-_-_----___---___----__'
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
flask_bcrypt = Bcrypt(app)

from application.users import models as user_models
from application.users.views import users

app.register_blueprint(users, url_prefix='/users')


@login_manager.user_loader
def load_user(user_id):
    return application.user_models.query.get(int(user_id))
