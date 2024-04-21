# A view function is the code you write to respond to requests to your application. 
# A Blueprint is a way to organize a group of related views and other code. 
# Rather than registering views and other code directly with an application, they are registered with a blueprint. 
# Then the blueprint is registered with the application when it is available in the factory function.

"""
from flask import Blueprint

bp = Blueprint('auth', __name__) 
#define a blueprint object named 'auth', second argument __name__ stands for where the blueprint is defined.


# to register the blueprint
def create_app():
    app = ...
    # existing code omitted

    from . import auth
    app.register_blueprint(auth.bp)

    return app

"""

import flask_login
from flask import Blueprint, render_template, request, redirect, url_for, session, render_template_string
from werkzeug.security import check_password_hash
import database as db

login_bp = Blueprint('auth', __name__, template_folder="templates") 
users = db.users

# First difference of writing a view function with blueprint, is that the route decorator
# comes from the blueprint object.
@login_bp.route("/login", methods = ['GET', 'POST'])
def login_get():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        user = users.get(request.form["email"])  
        if user is None or not check_password_hash(user.password, request.form["password"]):
            return redirect(url_for("auth.login_get")) 
        # Second difference, to allow different blueprints to define view functions with the same endpoints(urls), 
        # as well as to avoid collision, a namespace to all the endpoints from a blueprint is automatically assigned.

        flask_login.login_user(user)
        return redirect(url_for("auth.index"))


@login_bp.route("/index")
@flask_login.login_required
def index():
    return render_template_string(
        "You are logged in as: {{ current_user.id }}. \n Showing content that's only viewable by you."
    )


@login_bp.route("/logout")
def logout():
    flask_login.logout_user() 
    return "Logged out"


@login_bp.route("/session")
def get_session():
	return session._get_current_object()
