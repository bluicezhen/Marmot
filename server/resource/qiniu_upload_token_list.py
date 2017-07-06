import time
from hashlib import md5
from flask import g
from flask_restful import Resource
from flask_cors import cross_origin
from server.service import ServiceQiNiu
from server.public.dec import auth_params_url, resource


class ResourceUserQiNiuUploadTokenList(Resource):
    @cross_origin()
    @resource()
    @auth_params_url(params_except=["file_name"])
    def get(self, user_uid: int) -> dict:
        seed = md5(str(time.time()).encode('utf-8')).hexdigest()
        file_name = f"user/{user_uid}/{seed}/{g.params['file_name']}"
        token, url = ServiceQiNiu().get_upload_token(file_name)

        return {
            "upload_key": file_name,
            "upload_token": token,
            "url": url,
        }
