from flask_restx import Resource, Namespace

ns = Namespace('api')

@ns.route('/events')
class Events(Resource):

    def get(self):
        return "OK", 200

    def post(self, data):
        return "OK", 201


@ns.route('/search')
class Events(Resource):

    def post(self, data):
        return "OK", 201
