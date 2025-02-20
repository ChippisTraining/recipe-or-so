from flask import Flask, render_template

def create_app():
    app = Flask(__name__)
    
    from .routes.public import public
    
    app.register_blueprint(public)
    
    @app.errorhandler(404) 
    def not_found(e): 
        return render_template("404.html") 
    
    return app
