from flask import Flask
from config import DevelopmentConfig
from app.celery_instance import configure_celery


def create_app(config=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config)

    # register main blueprint
    from app.main import main as main_bp
    app.register_blueprint(main_bp)

    # register error blueprint
    # from app.errors import errors as errors_bp
    # app.register_blueprint(errors_bp)

    # configure celery
    cel_app = configure_celery(app)

    return app
