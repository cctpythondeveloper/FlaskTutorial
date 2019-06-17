from flask import Blueprint
from flask import request, render_template, flash, session

from myapp.controller.todos_controller import search_todotbs
from myapp.controller.users_controller import insert_user, search_user_by_id
from myapp.views.view import login_required

user = Blueprint('user', __name__)

@user.route('/register', methods=['GET', 'POST'])
def to_register_user():
    if request.method == 'GET':
        return render_template('user/register_user.html')

    username = request.form['username']
    password = request.form['password']
    if not username:
        flash('Invalid username')
        return render_template('user/register_user.html')
    elif not password:
        flash('Invalid password')
        return render_template('user/register_user.html')
    if insert_user(username, password):
        flash('Success Register User')
        return render_template('login.html')
    else:
        flash('User Name multiply Error')
        return render_template('user/register_user.html')

@user.route('/')
@login_required
def show_user_toppage():
    user = search_user_by_id(session['user_id'])
    todos = search_todotbs()
    return render_template('user/toppage.html', user=user, todos=todos)