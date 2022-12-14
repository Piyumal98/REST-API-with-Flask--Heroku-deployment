from flask import Flask
from firebase_admin import credentials, initialize_app

cred = credentials.Certificate("E:/Edu/py/REST API with Flask- Heroku deployment/api/Key.json")
default_app = initialize_app(cred)

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '123pyflfb'

    from .userAPI import userAPI

    app.register_blueprint(userAPI, url_prefix='/user')

    return app 