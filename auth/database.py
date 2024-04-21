import flask_login
from flask_login import login_manager, UserMixin
from werkzeug.security import generate_password_hash

login_manager = flask_login.LoginManager()

class User(UserMixin): 
    def __init__(self, email, password):
        self.id = email
        self.password = password

users = {
	"mxu@ut.edu": User("mxu@ut.edu", generate_password_hash("secret")),
    "apple@ut.edu": User("apple@ut.edu", generate_password_hash("apple"))
}

# User loader callback function is required by Flask_Login; it returns either None or the authenticated user object.
# given the id string, this call back function returns the User object from the users dictionary
@login_manager.user_loader 
def user_finder(id):
    return users.get(id)