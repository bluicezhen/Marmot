from datetime import datetime
from flask import g
from flask_cors import cross_origin
from flask_restful import Resource
from server.db import DBSession
from server.exc import ExceptionResponse
from server.model import ModelEvent
from server.public.dec import auth_params_body, auth_permission, resource


class ResourceEventL(Resource):
    @cross_origin()
    @resource()
    @auth_permission(["user"])
    @auth_params_body(params_except=["title", "desc", "time_begin", "time_end"])
    def post(self):
        user_uuid = g.user.get('uuid')
        try:
            title = g.params["title"]  # type: str
            desc = g.params["desc"]  # type: str
            time_begin = datetime.fromtimestamp(int(g.params["time_begin"]))  # type: datetime
            time_end = datetime.fromtimestamp(int(g.params["time_end"]))  # type: datetime

            with DBSession() as db_session:
                event = ModelEvent(db_session).create_one(user_uuid, title, desc, time_begin, time_end)
                return event.to_dict()

        except ValueError:
            ExceptionResponse(400, "Illegality Timestamp Type")
