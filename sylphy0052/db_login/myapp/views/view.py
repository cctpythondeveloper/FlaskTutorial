"""
Program for View
"""

from flask import request, redirect, url_for, render_template, flash, session
from myapp import app
from functools import wraps

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
        if request.form['username'] != app.config['USERNAME']:
            flash('Invalid User Name')
        elif request.form['password'] != app.config['PASSWORD']:
            flash('Invalid Password')
        else:
            session['logged_in'] = True
            flash('Login Success!')
            return redirect(url_for('show_toppage', username=request.form['username']))
    # Get Process
    return render_template('login.html')

# logout method
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('Logout')
    return redirect(url_for('login'))

@app.route('/<username>')
@login_required
def show_toppage(username):
    return render_template('toppage.html', username=username)
