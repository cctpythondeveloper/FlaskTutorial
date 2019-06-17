from flask import flash
from sqlalchemy.exc import IntegrityError

from myapp import db
from myapp.models.todos import Todo


def insert_todotb(title, content, todo_date, user_id):
    todo = Todo(
        title=title,
        content=content,
        todo_date=todo_date,
        user_id=user_id
    )
    try:
        db.session.add(todo)
        db.session.commit()
    except IntegrityError:
        return False
    return True

def search_todotbs():
    todos = db.session.query(Todo).\
        all()
    return todos

def update_todotb(id, title, content, todo_date):
    todo = Todo.query.get(id)
    todo.title = title
    todo.content = content
    todo.todo_date = todo_date
    db.session.merge(todo)
    db.session.commit()
    flash('Update Todo!')
    return True

def delete_todotb(id):
    todo = Todo.query.get(id)
    db.session.delete(todo)
    db.session.commit()
    flash('Delete Todo!')