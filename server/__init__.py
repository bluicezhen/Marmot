import conf
from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from . import resource


def create_app():
    debug = conf.debug
    app = Flask(__name__)
    CORS(app)
    app.debug = debug
    api = Api(app=app)

    api.add_resource(resource.ResourceEventL, "/event")
    api.add_resource(resource.ResourceUserL, "/user")
    api.add_resource(resource.ResourceUserToken, "/user_token")

    return app
