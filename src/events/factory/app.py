from flask import Flask
from dynaconf import FlaskDynaconf
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from src.events.adapters import celery


db = SQLAlchemy()
migrate = Migrate()


def create_app(**config):
    app = Flask(__name__)
    #configs for dynaconf
    FlaskDynaconf(app, **config)

    #DB
    db.init_app(app)
    migrate.init_app(app, db)

    # register api
    from src.events.entrypoints.flask_app import blueprint_event
    from src.events.adapters.rest_lib import api
    app.register_blueprint(blueprint_event, url_prefix="/api")
    api.init_app(app)

    #celery
    celery.init_app(app)

    return app
