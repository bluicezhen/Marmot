from server.db import ExceptionDB, TableUser
from server.public.func import password_hash_salt
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
            user = self.session.query(TableUser) \
                .filter(TableUser.username == username) \
                .one()  # type: TableUser
            password_hash = password_hash_salt(password, user.time_create)
            if password_hash != user.password:
                raise ExceptionDB("NOT_FOUND")
            return user
        except NoResultFound:
            raise ExceptionDB("NOT_FOUND")

    def find_one_by_uuid(self, uuid: str) -> TableUser:
        try:
            return self.session.query(TableUser).filter(TableUser.uuid == uuid).one()
        except NoResultFound:
            raise ExceptionDB("NOT_FOUND")
