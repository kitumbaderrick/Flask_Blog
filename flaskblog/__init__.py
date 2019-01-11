from flask import Flask
from flask_sqlalchemy import SQLAlchemy


 
app = Flask(__name__)
app.config['SECRET_KEY'] = '708390d1213664820859edcecfb9c23e'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

from flaskblog import routes