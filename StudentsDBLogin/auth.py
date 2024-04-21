import flask_login
from flask import Blueprint, request, redirect, url_for
import database
from werkzeug.security import check_password_hash

students = database.students

db = Blueprint('login', __name__)
    
@db.get("/login")
def login_get():
    return """<form method=post>
      StudentId: <input name="id"><br>
      Password: <input name="password" type=password><br>
      <button>Log In</button>
    </form>"""


@db.post("/login")
def login_post():
    id = request.form.get("id")
    user = database.user_finder(id)
    if user is None or not check_password_hash(user.password, request.form.get("password")):
        return redirect(url_for("login.login_get"))

    flask_login.login_user(user)
    return redirect(url_for("login.index"))

@db.route("/index")
@flask_login.login_required
def index():
    return f"You are logged in. \n Showing content that's only viewable by you."


@db.route("/logout")
def logout():
    flask_login.logout_user() 
    return "Logged out"



