from server.db import ExceptionDB, TableUser
from sqlalchemy.orm.exc import NoResultFound
from ._model import Model


class ModelUser(Model):
    def create_one(self, username: str, password: str, nickname: str) -> TableUser:
        user = TableUser(username, password, nickname)
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user

    def find_one_by_username_password(self, username: str, password: str) -> TableUser:
        try:
            return self.session.query(TableUser) \
                .filter(TableUser.username == username, TableUser.password == password) \
                .one()
        except NoResultFound:
            raise ExceptionDB("NOT_FOUND")
