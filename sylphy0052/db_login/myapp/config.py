"""
config file
"""

import os

# Debug mode turn on
DEBUG = True

# database
SQLALCHEMY_DATABASE_URI = 'sqlite:///usertb.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True

# Config secret key
SECRET_KEY = os.urandom(24)

# For Test
USERNAME = 'test'
PASSWORD = 'test'
