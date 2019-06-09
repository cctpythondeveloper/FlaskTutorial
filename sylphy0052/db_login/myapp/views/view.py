"""
Program for View
"""

from flask import request, redirect, url_for, render_template, flash, session
from myapp import app
from functools import wraps
from myapp.controller.dbcontroller import insert_user, search_user_for_login

# check login
def login_required(view):
    @wraps(view)
    def inner(*args, **kwargs):
        if not session.get('logged_in'):
            return redirect(url_for('login'))
        return view(*args, **kwargs)
    return inner

# login method
@app.route('/login', methods=['GET', 'POST'])
def login():
    # Post Process
    if request.method == 'POST':
        if not request.form['username']:
            flash('Input User Name')
        elif not request.form['password']:
            flash('Input Password')
        else:
            users = search_user_for_login(request.form['username'], request.form['password'])
            if len(users) == 1:
                session['logged_in'] = True
                flash('Login Success!')
                return redirect(url_for('user.show_toppage', userid=users[0].id))
            else:
                flash('Invalid User Name or Password')

    return render_template('login.html')

# logout method
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('Logout')
    return redirect(url_for('login'))

@app.route('/add', methods=['GET', 'POST'])
def add_user():
    # GET
    if request.method == 'GET':
        return render_template('add.html')
    # POST
    username = request.form['username']
    password = request.form['password']
    if not username:
        flash('Invalid username')
        return render_template('add.html')
    elif not password:
        flash('Invalid password')
        return render_template('add.html')
    if insert_user(username, password):
        flash('Success Register User')
        return render_template('login.html')
    else:
        flash('User Name multiply Error')
        return render_template('add.html')
