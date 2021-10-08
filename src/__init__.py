from flask import Flask
from dynaconf import FlaskDynaconf
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


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
    from src.events.entrypoints import api
    api.init_app(app)

    return app
