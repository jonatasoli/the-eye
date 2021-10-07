from flask import Flask


def create_app():
    app = Flask(__name__)

    # register api
    from src.events.entrypoints import api

    api.init_app(app)

    return app
