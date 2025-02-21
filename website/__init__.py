from flask import Flask, render_template
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")
SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI", "sqlite:///database.db")
SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS", "False").lower() == "true"

def create_db(app):
    app.config['SECRET_KEY'] = SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS

    db = SQLAlchemy(app)

    with app.app_context():
        db.create_all()

def create_app():
    app = Flask(__name__)

    create_db(app)
    
    from .routes.public import public
    from .routes.api import api
    from .routes.auth import auth
    
    app.register_blueprint(public, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(api, url_prefix='/api')

    @app.errorhandler(404) 
    def not_found(e): 
        return render_template("404.html")
    
    return app
