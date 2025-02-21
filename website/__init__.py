from flask import Flask, render_template

def create_app():
    app = Flask(__name__)
    
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
