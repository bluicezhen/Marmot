from datetime import datetime
from flask import g
from flask_cors import cross_origin
from flask_restful import Resource
from server.exc import ExceptionResponse
from server.model import ModelEvent
from server.public.dec import auth_params_body, db_session, resource


class ResourceEventL(Resource):
    @cross_origin()
    @resource()
    @auth_params_body(params_except=["title", "desc", "time_begin", "time_end"])
    @db_session()
    def post(self):
        try:
            title = g.params["title"]  # type: str
            desc = g.params["desc"]  # type: str
            time_begin = datetime.fromtimestamp(int(g.params["time_begin"]))  # type: datetime
            time_end = datetime.fromtimestamp(int(g.params["time_end"]))  # type: datetime

            event = ModelEvent(g.db_session).create_one(title, desc, time_begin, time_end)

            return event.to_dict()
        except ValueError:
            ExceptionResponse(400, "Illegality Timestamp Type")
