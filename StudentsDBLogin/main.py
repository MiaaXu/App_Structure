from flask import Flask
# import flask_login
import database
from add_student import add_bp
from auth import db
from dotenv import load_dotenv
load_dotenv()
import os

login_manager = database.login_manager

def create_app():
    app = Flask(__name__)
    login_manager.init_app(app)
    app.secret_key = os.getenv('secrect_key')

    app.register_blueprint(add_bp)
    app.register_blueprint(db)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug = True)