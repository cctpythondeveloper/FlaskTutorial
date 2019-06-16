from myapp import db
from sqlalchemy.orm import relationship


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    password = db.Column(db.String(30))
    todo = relationship("Todo", backref="user", lazy="dynamic")

    def __init__(self, name=None, password=None):
        self.name = name
        self.password = password
