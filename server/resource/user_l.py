from flask import g
from flask_cors import cross_origin
from flask_restful import Resource
from server.model import ModelUser
from server.public.dec import auth_params_body, db_session
from typing import Dict, Union


class ResourceUserL(Resource):
    @cross_origin()
    @auth_params_body(params_except=["username", "password", "nickname"])
    @db_session()
    def post(self) -> Dict[str, Union[str, int]]:
        return ModelUser(g.db_session).create_one(g.params["username"], g.params["password"], g.params["nickname"]) \
            .to_dict()
