"""
Initialize Program
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Import config from config files
app.config.from_object('myapp.config')

# Database
db = SQLAlchemy(app)

# user
from myapp.views.user import user
app.register_blueprint(user, url_prefix='/user')

from myapp.views import view, user
