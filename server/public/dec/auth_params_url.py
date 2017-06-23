import wrapt
from flask import g, request
from server.exc import ExceptionResponse
from typing import List


def auth_params_url(params_except: List[str]=None, params_option: List[str]=None):
    @wrapt.decorator
    def decorated_function(wrapped, instance, args, kwargs):
        g.params = {}
        url_params = request.args
        if params_except:
            for param in params_except:
                param_val = url_params.get(param)
                if param_val:
                    g.params[param] = param_val
                else:
                    raise ExceptionResponse(401, "Illegal Parameter")
        if params_option:
            for param in params_option:
                g.params[param] = url_params.get(param)
        return wrapped(*args, **kwargs)

    return decorated_function
