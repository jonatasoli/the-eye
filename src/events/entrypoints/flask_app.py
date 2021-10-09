import json
from loguru import logger
from flask import Blueprint
from flask_restx import Resource, Namespace
from datetime import datetime

from src.events.adapters.rest_lib import api
from src.events.adapters.api_model import post_event, event_response, \
    search_response, search_event


from src.events.domain.model import Event, HostData


# api = Api(version="1.0", title="Events API", doc="/doc")
# ns = Namespace('api')
# api.add_namespace(ns, path="/api")
blueprint_event = Blueprint('api', __name__, url_prefix='/api/1') # This blueprint is not used
ns = api.namespace('api')


def get_service_events():
    from src.events.services import service_layer, unit_of_work
    return service_layer.ServiceEvents()
def get_uow():
    from src.events.services import service_layer, unit_of_work
    return unit_of_work.SqlAlchemyUnitOfWork()

def get_broker():
    from src.events.adapters.queue import AbstractBroker, Broker
    return Broker()


@ns.route('/events')
class Events(Resource):
    """Send events to the eye"""

    @ns.doc('send event')
    @ns.expect(post_event)
    @ns.marshal_with(event_response, code=204)
    def post(
        self,
        service=get_service_events(),
        broker=get_broker()
        ):
        try:
            input_data = api.payload
            _event = Event(
                session_id=input_data.get('session_id'),
                category=input_data.get('category'),
                name=input_data.get('name'),
                data=HostData(
                    host=input_data.get('host'),
                    path=input_data.get('path'),
                    element=input_data.get('element'),
                    form=input_data.get('form'),
                ),
                timestamp=input_data.get('timestamp'),
            )
            return service.enqueue_event(event=_event, enqueue=broker), 204
        except Exception as e:
            logger.error(f"Erro: {e}")
            return api.abort(400, "Error to process this request")


@ns.route('/search')
class SearchEvents(Resource):

    @ns.doc('search events list')
    @ns.expect(search_event)
    def post(
        self,
        service=get_service_events(),
        uow=get_uow()
    ):
        try:
            input_data = api.payload
            _session_id = input_data.get('session_id')
            _category = input_data.get('category')
            _start_date = input_data.get('start_date')
            _end_date = input_data.get('end_date')
            if _session_id:
                _result = service.search_session(
                    session_id = _session_id,
                    uow = uow
                ), 200
            elif _category:
                _result =service.search_category(
                    category = _category,
                    uow = uow
                ), 200
            elif _start_date and _end_date:
                _result =service.search_data_range(
                    start_date = datetime.strptime(_start_date, Event.get_format_timestamp()),
                    end_date = datetime.strptime(_end_date, Event.get_format_timestamp()),
                    uow = uow
                ), 200
            else:
                return api.abort(200, "Params not found")
            return {"events": _result}, 200

        except Exception as e:
            logger.error(f"Erro: {e}")
            return api.abort(400, "Error to process this request")
