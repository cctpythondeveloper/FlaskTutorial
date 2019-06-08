from flask import Flask
from flask import Flask,flash,redirect,render_template,request,session,abort

app = Flask(__name__)
app.secret_key="test"
username = "test"
password = "test"

@app.route("/")
def home():
    if not session.get("logged_in"):
        return render_template("login.html")
    else:
        return render_template("success.html",username=username,password=password)

@app.route("/login", methods=["POST"])
def login():
    if request.form["username"] == username \
        and request.form["password"] == password:
        session["logged_in"] = True
    else:
        flash('wrong password!')
    return home()

@app.route("/logout",methods=["POST"])
def logout():
    session["logged_in"] = False
    return home()

if __name__ == "__main__":
    app.run()
