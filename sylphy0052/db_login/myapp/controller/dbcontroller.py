"""
DBController
insert / update / delete / search
"""

from myapp import db
from myapp.models.user import User
from sqlalchemy.exc import IntegrityError

def insert_user(username, password):
    user = User(
        username = username,
        password = password
    )
    try:
        db.session.add(user)
        db.session.commit()
    except IntegrityError: # Unique key multiply
        return False
    return True

def search_user_for_login(username, password):
    # sql = 'select * from usertb where username={} and password={}'.format(username, password)
    users = db.session.query(User).\
        filter(User.username==username).\
        filter(User.password==password).\
        all()
    return users

def search_user_by_id(id):
    users = db.session.query(User).\
        filter(User.id==id).\
        all()
    return users[0]
