from flask import Blueprint, request, render_template
from werkzeug.security import generate_password_hash
import database 

add_bp = Blueprint('register', __name__, template_folder= 'templates')
students = database.students

@add_bp.route('/addstudent', methods = ['GET', 'POST'])
def student_post():
    if request.method == 'GET': 
        print('Welcome to student page.')

    elif request.method == 'POST': 
        name = request.form.get('name') 
        id = request.form.get('id')
        email = request.form.get('email')
        password = request.form.get('password')
        enroll_date = request.form.get('enrollment')
        
        # check primary key id is not missing
        if id == '':
            return 'Error: Missing Student Id.'
      
        # check duplicate primary key
        cursor = students.cursor()
        query = f"Select StudentID From Students"
        cursor.execute(query)
        a = cursor.fetchall()
        print(a)
        for student_id in a:
                if id == student_id[0]:
                    return 'Error: Student Exists.'

        q = "INSERT INTO Students (Name, StudentID, Email, Password, Enrollment) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(q, (name, id, email, generate_password_hash(password), enroll_date))
        students.commit()
        cursor.close()


    return render_template('students.html' )