from flask import request, redirect, url_for, render_template, flash, session
from flask import Blueprint
from myapp.controller.users_controller import insert_user
from myapp.views.view import login_required
from myapp.controller.users_controller import search_user_by_id

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

@user.route('/<int:userid>')
@login_required
def show_user_toppage(userid):
    user = search_user_by_id(userid)
    return render_template('user/toppage.html', user=user)