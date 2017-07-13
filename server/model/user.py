from server.db import TableUser
from ._model import Model


class ModelUser(Model):
    def create_one(self, username: str, password: str, nickname: str) -> TableUser:
        user = TableUser(username, password, nickname)
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user
