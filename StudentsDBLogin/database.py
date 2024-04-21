import mysql.connector 
import flask_login

students = mysql.connector.connect(user = 'root',
                        password = '1234abcd',
                        database = 'StudentsDB')


login_manager = flask_login.LoginManager()

class User(flask_login.UserMixin): 
    def __init__(self, studentid, password):
        self.id = studentid
        self.password = password

@login_manager.user_loader 
def user_finder(id):
    cursor = students.cursor()
    cursor.execute('SELECT StudentID, Password from Students where StudentID = %s', (id,) )
    user = cursor.fetchone()
    cursor.close()
    if user is not None:
        return User(user[0], user[1])
    else:
        return None


