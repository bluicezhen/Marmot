import wrapt
from flask import g, request
from server.exc import ExceptionResponse


def auth_params_body(params_except=None, params_option=None):
    @wrapt.decorator
    def decorated_function(wrapped, instance, args, kwargs):
        data = request.get_json()
        g.params = {}
        if params_except is not None:
            if data is None:
                raise ExceptionResponse(401, "Illegal Parameter")
            try:
                for key in params_except:
                    g.params[key] = data[key]
            except KeyError:
                raise ExceptionResponse(401, f"Necessary Parameters: {key}")
            try:
                for key in params_option:
                    g.params[key] = data[key]
            except KeyError:
                pass
            except TypeError:
                pass
        if params_option is not None:
            for key in params_option:
                try:
                    g.params[key] = data[key]
                except KeyError:
                    g.params[key] = None
        return wrapped(*args, **kwargs)

    return decorated_function
