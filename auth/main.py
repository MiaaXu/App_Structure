import flask
from auth import login_bp
import database as db

from dotenv import load_dotenv
load_dotenv()  # to read the .env file 
import os


login_manager = db.login_manager

def create_app():
    app = flask.Flask(__name__)
    # app.secret_key = "super secret string"
    app.secret_key = os.getenv('secrect_key')
    
    login_manager.init_app(app)
    app.register_blueprint(login_bp)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)