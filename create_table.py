from server.db import engine, TableEvent

if __name__ == "__main__":
    TableEvent.__table__.create(bind=engine)
