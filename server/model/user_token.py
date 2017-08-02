from server.db import TableUserToken
from ._model import Model


class ModelUserToken(Model):
    def create_one(self, user_uuid: str) -> TableUserToken:
        user_token = TableUserToken(user_uuid)
        self.session.add(user_token)
        return user_token
