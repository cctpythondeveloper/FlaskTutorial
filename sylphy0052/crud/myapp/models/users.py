from myapp import db
from sqlalchemy.orm import relationship
from myapp.models.todos import Todo

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    password = db.Column(db.String(30))
    todos = relationship(Todo)

    def __init__(self, name=None, password=None):
        self.name = name
        self.password = password
        # self.todos = None
