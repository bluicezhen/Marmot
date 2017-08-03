from flask import g
from flask_cors import cross_origin
from flask_restful import Resource
from server.db import DBSession, ExceptionDB
from server.exc import ExceptionResponse
from server.model import ModelUser, ModelUserToken
from server.public.dec import auth_params_body, resource


class ResourceUserToken(Resource):
    @cross_origin()
    @resource()
    @auth_params_body(params_except=["username", "password"])
    def post(self) -> dict:
        username = g.params["username"]
        password = g.params["password"]
        try:
            with DBSession() as db_session:
                user = ModelUser(db_session).find_one_by_username_password(username, password)
                return ModelUserToken(db_session).create_one(user.uuid)
        except ExceptionDB as e:
            if e.type == "NOT_FOUND":
                raise ExceptionResponse(400, "Username/Password Error!")
