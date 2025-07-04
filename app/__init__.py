from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    
    return app