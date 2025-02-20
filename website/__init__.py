from flask import Flask

def create_app():
    app = Flask(__name__)
    
    from .routes.public import public
    
    app.register_blueprint(public)
    
    return app
