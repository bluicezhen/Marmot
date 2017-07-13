from server.db import engine, TableEvent, TableUser, TableUserToken

if __name__ == "__main__":
    TableEvent.__table__.create(bind=engine)
    TableUser.__table__.create(bind=engine)
    TableUserToken.__table__.create(bind=engine)
