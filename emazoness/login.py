from flask import Flask, render_template, redirect, url_for,request,session
from flask_login import LoginManager, login_user, login_required

app = Flask(__name__)
app.secret_key = "secret key"

login_manager = LoginManager()
login_manager.init_app(app)

@app.route("/", methods=["GET"])
def form():
    print("form do")
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    print("login do")
    if request.form["username"] == "test" \
        and request.form["password"] == "test":
        print("dashboard")
        return render_template("dashboard.html")
    else:
        return form()

# @app.route("/dashboard", methods=["GET"])
# def dashboard():
#     print("tinko")
#     return

@login_manager.user_loader
def load_user(user_id):
    return User()

if __name__ == "__main__":
    app.run()
