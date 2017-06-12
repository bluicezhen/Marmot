from flask_restful import Resource


class ResourceImage(Resource):
    def get(self, image_uid: str) -> object:
        pass

    def delete(self, image_uid: str) -> object:
        pass
