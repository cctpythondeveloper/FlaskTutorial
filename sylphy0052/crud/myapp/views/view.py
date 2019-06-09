from flask import request, redirect, url_for, render_template, flash, session
from myapp import app
from functools import wraps

# check login
def login_required(view):
    @wraps(view)
    def inner(*args, **kwargs):
        if not session.get('logged_in'):
            return redirect(url_for('to_login'))
        return view(*args, **kwargs)
    return inner

@app.route('/')
def toppage():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    pass

@app.route('/logout')
def logout():
    pass

@app.route('/register_user', methods=['GET', 'POST'])
def register_user():
    if request.method == 'GET':
        return render_template('register_user.html')
    else:
        pass
