from flask import Flask, render_template
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")
SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI", "sqlite:///database.db")
SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS", "False").lower() == "true"

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    """Create and configure the Flask app"""
    app = Flask(__name__)

    app.config['SECRET_KEY'] = SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    from .models.user import User
    
    with app.app_context():
        db.create_all()


    @login_manager.user_loader
    def load_user(user_id):
        """Loads user for Flask-Login"""
        return User.query.get(int(user_id))

    from .routes.public import public
    from .routes.api import api
    from .routes.auth import auth

    app.register_blueprint(public, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(api, url_prefix='/api')

    @app.errorhandler(404)
    def not_found(e):
        return render_template("404.html"), 404

    return app
