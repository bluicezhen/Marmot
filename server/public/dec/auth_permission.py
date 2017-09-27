import wrapt
from conf import debug
from flask import g, request
from server.exc import ExceptionResponse
from server.model import ModelUser, ModelUserToken
from server.db import DBSession, ExceptionDB

MODEL_ADMIN = 0
MODEL_USER = 1


def auth_permission(permission_model_l):
    @wrapt.decorator
    def decorated_function(wrapped, instance, args, kwargs):
        user_uuid = request.headers.get("User-UUID")
        token = request.headers.get("Token")

        if not user_uuid or not token:
            raise ExceptionResponse(403, "NOT Logged In")
        if token.startswith("admin:"):
            g.permission_model = MODEL_ADMIN
        else:
            g.permission_model = MODEL_USER

        if "user" in permission_model_l and g.permission_model == MODEL_USER:
            _auth_user(user_uuid, token)

        return wrapped(*args, **kwargs)

    return decorated_function


def _auth_user(user_uuid: str, token: str):
    try:
        with DBSession() as db_session:
            if debug:
                g.user = ModelUser(db_session).find_one_by_uuid(user_uuid).to_dict()
            else:
                if ModelUserToken(db_session).update_one_by_user_uuid_token_latest(user_uuid, token) <= 0:
                    db_session.rollback()
                    raise ExceptionResponse(403, "NOT Logged In")
                g.user = ModelUser(db_session).find_one_by_uuid(user_uuid).to_dict()
                db_session.commit()
    except ExceptionDB as e:
        if e.type == "NOT_FOUND":
            raise ExceptionResponse(403, "Illegal User")
