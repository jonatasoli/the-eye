from flask import Flask
from flask_restx import Api, Resource, fields

app = Flask(__name__)

api = Api(app, version='1.0', title='The EYE API',
    description='Get events API',
)
ns = api.namespace('api', description='events endpoint')

@ns.route('/events')
class Events(Resource):

    def get(self, id):
        return "OK", 200

    def post(self, data):
        return "OK", 201


# @app.route("/send_events", methods=["POST"])
# def send_events():
#     """Except unexpect value in the payload"""
#     """Except invalid timestamp"""
#     return "OK", 201


# @app.route("/search/}", methods=["GET"])
# def search():
#     """
#     params:
#         session
#         category
#         time range>>
#             time-start=2021-01-01 09:15:27.243860
#             time-end=2021-01-02 10:15:27.243860

#     """
#     return "OK", 200
