# Initialize Flask object
from flask import Flask

app = Flask(__name__)
app.config.from_object('myapp.config')

# DB
SQLALCHEMY_DATABASE_URI = 'sqlite:///crud.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

from myapp.views import view
