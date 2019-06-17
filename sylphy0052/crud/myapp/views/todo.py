from datetime import datetime as dt

from flask import Blueprint
from flask import request, render_template, flash, session, url_for, redirect

from myapp.controller.todos_controller import insert_todotb, update_todotb, delete_todotb
from myapp.models.todos import Todo
from myapp.views.view import login_required

todo = Blueprint('todo', __name__)

@todo.route('/register', methods=['GET', 'POST'])
@login_required
def register_todo():
    if request.method == 'GET':
        current_date = dt.now().strftime('%Y-%m-%d')
        return render_template('todo/register_todo.html', current_date=current_date)

    title = request.form['title']
    content = request.form['content']
    todo_date = dt.strptime(request.form['tododate'], '%Y-%m-%d')

    if not title:
        flash('Invalid title')
        return render_template('todo/register_todo.html')
    elif not content:
        flash('Invalid content')
        return render_template('todo/register_todo.html')
    elif not todo_date:
        flash('Invalid Todo Date')
        return render_template('todo/register_todo.html')

    if insert_todotb(title, content, todo_date, session['user_id']):
        flash('Success Register Todo')
        return redirect(url_for('user.show_user_toppage'))
    else:
        flash('Error')
        return render_template('todo/register_todo.html')

@todo.route('/detail/<int:id>')
@login_required
def show_detail(id):
    todo = Todo.query.get(id)
    return render_template('todo/detail_todo.html', todo=todo)

@todo.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_todo(id):
    if request.method == 'GET':
        todo = Todo.query.get(id)
        return render_template('todo/update_todo.html', todo=todo)

    title = request.form['title']
    content = request.form['content']
    todo_date = dt.strptime(request.form['tododate'], '%Y-%m-%d')

    if not title:
        flash('Invalid title')
        return render_template('todo/update_todo.html', id=id)
    elif not content:
        flash('Invalid content')
        return render_template('todo/update_todo.html', id=id)
    elif not todo_date:
        flash('Invalid Todo Date')
        return render_template('todo/update_todo.html', id=id)

    if update_todotb(id, title, content, todo_date):
        return redirect(url_for('user.show_user_toppage'))
    else:
        flash('Error')
        return render_template('todo/update_todo.html', id=id)

@todo.route('/delete/<int:id>', methods=['POST'])
@login_required
def delete_todo(id):
    delete_todotb(id)
    return redirect(url_for('user.show_user_toppage'))
