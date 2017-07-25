import os
from contextlib import ContextDecorator
from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker
from .event import TableEvent
from .user import TableUser
from .user_token import TableUserToken
from ._exc import DBException

engine = create_engine(f"sqlite:///{os.getcwd()}/marmot.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()


class DBSession(ContextDecorator):
    def __init__(self):
        self._handle_exc_d = self._handle_exc()
        self.ignore_exc = False
        self.session = Session()

    def __enter__(self):
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type in [IntegrityError]:
            self.ignore_exc = True
            self.session.rollback()
            self._handle_exc_d[exc_type](exc_val)
        else:
            self.session.commit()
        self.session.close()
        return self.ignore_exc

    def _handle_exc(self) -> dict:
        return {
            IntegrityError: self._handle_integrity_error
        }

    @staticmethod
    def _handle_integrity_error(exc_val):
        v = str(exc_val)
        if "UNIQUE" in v:
            field = v.split("UNIQUE constraint failed: ")[1].split(" [SQL:")[0].split(".")[1]
            raise DBException("UNIQUE", field=field)
