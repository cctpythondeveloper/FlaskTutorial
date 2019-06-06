from flask import Flask, request, session, redirect, url_for, render_template, flash

#configuration
DEBUG = True
SECRET_KEY = 'secret key'
USERNAME = 'test'
PASSWORD = 'test'

app = Flask(__name__)
app.config.from_object(__name__)

class UserInfo():
    username = None
    password = None
    def __init__(self, username, password):
        self.username = username
        self.password = password

@app.route('/', methods=['GET'])
def form():
    return render_template('index.html')

@app.route('/login', methods={'POST'})
def login():
    error = None
    if request.form['username'] != app.config['USERNAME']:
        error = 'Invalid username'
    elif request.form['password'] != app.config['PASSWORD']:
        error = 'Invalid password'
    else:
        session['logged_in'] = True
        userinfo = UserInfo(username=request.form['username'],
                            password=request.form['password'])
        return render_template('toppage.html', userinfo=userinfo)
    return render_template('index.html', error=error)


if __name__ == '__main__':
    app.run()

#render_template('表示するページ', 使用する値)