from server.db import engine, TableEvent

TableEvent.__table__.create(bind=engine)
