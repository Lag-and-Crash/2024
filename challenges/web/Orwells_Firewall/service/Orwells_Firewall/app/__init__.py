from flask import Flask

from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp, url_prefix='/')

    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    return app