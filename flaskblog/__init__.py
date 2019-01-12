from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt 

 
app = Flask(__name__)
app.config['SECRET_KEY'] = '708390d1213664820859edcecfb9c23e'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

from flaskblog import routes