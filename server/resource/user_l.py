from flask import g
from flask_cors import cross_origin
from flask_restful import Resource
from server.db import DBException, DBSession
from server.exc import ExceptionResponse
from server.model import ModelUser
from server.public.dec import auth_params_body, resource
from typing import Dict, Union


class ResourceUserL(Resource):
    @cross_origin()
    @resource()
    @auth_params_body(params_except=["username", "password", "nickname"])
    def post(self) -> Dict[str, Union[str, int]]:
        try:
            with DBSession() as db_session:
                return ModelUser(db_session) \
                    .create_one(g.params["username"], g.params["password"], g.params["nickname"]) \
                    .to_dict()
        except DBException as e:
            if e.type == "UNIQUE" and e.field == "username":
                raise ExceptionResponse(400, "The username has been registered.")
            else:
                raise e
