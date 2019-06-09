"""
Initialize Program
"""

from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Import config from config files
app.config.from_object('myapp.config')

from myapp.views import view
