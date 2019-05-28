# -*- coding: utf-8 -*-

from flask import Flask, flash, redirect, render_template, request, session, url_for

# Configuration
DEBUG = True
SECRET_KEY = 'secret key'
USERNAME = 'test'
PASSWORD = 'test'

# Generation of Application
app = Flask(__name__)
app.config.from_object(__name__)

# Definition of User Information
class User():
    def __init__(self, username, password):
        self.username = username
        self.password = password

# If GET methods, transit to Login window.
@app.route('/', methods=['GET'])
def form():
    return render_template('login.html')

# Error check
@app.route('/login', methods=['POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('Succeeded in login!')
    return render_template('login.html', error=error)

# Logout
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('Logged out.')
    return redirect(url_for('login.html')) ######

if __name__ == '__main__':
    app.run()
