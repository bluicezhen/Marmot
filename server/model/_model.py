from sqlalchemy.orm.session import Session


class Model(object):
    def __init__(self, session: Session):
        self.session = session
