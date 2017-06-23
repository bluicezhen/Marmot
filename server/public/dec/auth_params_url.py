import wrapt
from flask import g, request
from server.exc import ExceptionResponse


def auth_params_url(params_except=None, params_option=None):
    @wrapt.decorator
    def decorated_function(wrapped, instance, args, kwargs):
        g.params = {}
        url_params = request.args
        for param in params_except:
            param_val = url_params.get(param)
            if param:
                g.params[param] = param_val
            else:
                raise ExceptionResponse(401, "")
        for param in params_option:
            g.params[param] = url_params.get(param)
        return wrapped(*args, **kwargs)

    return decorated_function
