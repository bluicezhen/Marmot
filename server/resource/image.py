from flask_restful import Resource
from server.public.dec import auth_params_body, resource


class ResourceUserImageList(Resource):
    def get(self) -> list:
        pass

    @resource()
    @auth_params_body(params_except=["name", "url"])
    def post(self) -> dict:
        pass
