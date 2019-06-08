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

@app.route('/', methods=['GET'])
def form():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    msg = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME'] or request.form['password'] != app.config['PASSWORD']:
            error_msg = 'Invalid username or password. Please try again!'
            return render_template('login.html', msg=error_msg)
        else:
            session['logged_in'] = True
            user = User(username=request.form['username'], password=request.form['password'])
            msg = 'Succeeded in login!'
            return render_template('index.html', msg=msg, user=user)
    return render_template('login.html', msg=msg)

if __name__ == '__main__':
    app.run()
