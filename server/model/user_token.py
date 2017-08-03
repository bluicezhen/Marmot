from conf import conf
from datetime import datetime, timedelta
from server.db import TableUserToken
from ._model import Model


class ModelUserToken(Model):
    def create_one(self, user_uuid: str) -> TableUserToken:
        user_token = TableUserToken(user_uuid)
        self.session.add(user_token)
        return user_token

    def update_one_by_user_uuid_token_latest(self, user_uuid: str, token: str) -> int:
        now = datetime.now()
        token_validity = conf()["token_validity"]
        return self.session.query(TableUserToken) \
            .filter(TableUserToken.user_uuid == user_uuid, TableUserToken.token == token,
                    TableUserToken.time_update > now - timedelta(seconds=token_validity)) \
            .update({TableUserToken.time_update: now})
