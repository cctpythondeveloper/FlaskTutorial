from flask_script import Command
from myapp import db
from myapp.models.user import User

class InitDB(Command):
    "create database"

    def run(self):
        db.create_all()
