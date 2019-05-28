#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask, redirect ,request

app = Flask(__name__)

@app.route("/")
def index():
#     who = request.args.get("name")
#     passwd = request.args.get("pass")
#     return str(who)+" "+str(passwd)
#
# @app.route("/login")
# def login():
    html= """
    <!DOCTYPE html>
    <html lang="ja">
    <head>
        <meta charset="UTF-8">
        <title>ログイン</title>
        <script src="http://html5shiv.googlecode.com/svn/trunk/html5.js"></script>
    </head>
    <body>

        <form action="/" method="get">
            <h1>Login</h1>
            <input type="text" name="name" placeholder="Username" required/>
            <input type="password" name="pass" placeholder="Password" required/>
            <button>Login</button>
        </form>

    </body>
    </html>
    """
    return html

if __name__ == "__main__":
    app.run(debug=True)
