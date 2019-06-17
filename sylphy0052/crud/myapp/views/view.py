from flask import request, redirect, url_for, render_template, flash, session
from myapp import app
from functools import wraps
from myapp.controller.users_controller import search_user_for_login
from datetime import timedelta

# check login
def login_required(view):
    @wraps(view)
    def inner(*args, **kwargs):
        if not session.get('logged_in'):
            return redirect(url_for('login'))
        return view(*args, **kwargs)
    return inner

@app.route('/')
def toppage():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if not request.form['username']:
            flash('Input User Name')
        elif not request.form['password']:
            flash('Input Password')
        else:
            users = search_user_for_login(request.form['username'], request.form['password'])
            if len(users) == 1:
                session.permanent = True
                app.permanent_session_lifetime = timedelta(minutes=30)
                session['logged_in'] = True
                session['user_id'] = users[0].id
                flash('Login Success!')
                return redirect(url_for('user.show_user_toppage'))
            else:
                flash('Invalid User Name or Password')
                return render_template('login.html')
    else:
        return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('user_id', None)
    flash('Logout')
    return redirect(url_for('login'))

