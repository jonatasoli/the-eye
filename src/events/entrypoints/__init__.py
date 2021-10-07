from flask_restx import Api

from .flask_app import ns

api = Api(version="1.0", title="Events API", doc="/doc")

api.add_namespace(ns, path="/api")
