import wrapt
from flask import g
from server.db import DBSession


def db_session():
    @wrapt.decorator
    def decorated_function(wrapped, instance, args, kwargs):
        g.db_session = DBSession()
        resp = wrapped(*args, **kwargs)
        g.db_session.close()
        return resp

    return decorated_function
