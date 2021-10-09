from flask_restx import fields
from .rest_lib import api


form = api.model("FormModel", {
    'first_name': fields.String,
    'last_name': fields.String
})
data = api.model("DataModel", {
    'host': fields.String,
    'path': fields.String,
    'element': fields.String(required=False),
    'form': fields.Nested(form, required=False)
})
post_event = api.model('EventModel', {
    'session_id': fields.String,
    'category': fields.String,
    'data': fields.Nested(
        data,
        description='Adicional fields'),
    'timestamp': fields.String,
})

event_response = api.model('ResponseModel', {
})

search_response = api.model('SearchResponse', {
    'events': fields.List(fields.Nested(post_event))
})


search_event = api.model('SearchModel', {
    'session_id': fields.String(required=False),
    'category': fields.String(required=False),
    'start_date': fields.String(required=False),
    'end_date': fields.String(required=False)
})
