from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://hvrgcxixtmjajb:c548436cdd0df0b4048ffa67fc04beda5d49e18b73bb0bf58e35f5b8a1f48247@ec2-50-17-255-120.compute-1.amazonaws.com:5432/de9rml1je07q27?sslmode=require'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category ='info'

from noteapp import routes