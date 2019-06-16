from myapp import db
from myapp.models.users import User
from sqlalchemy.exc import IntegrityError

def insert_user(name, password):
    user = User(
        name=name,
        password=password
    )
    try:
        db.session.add(user)
        db.session.commit()
    except IntegrityError:
        return False
    return True

def search_user_for_login(name, password):
    users = db.session.query(User).\
        filter(User.name == name, User.password == password).\
        all()
    return users

def search_user_by_id(id):
    users = db.session.query(User).\
        filter(User.id == id).\
        all()
    return users[0]