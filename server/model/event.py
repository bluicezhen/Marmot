from datetime import datetime
from server.db import TableEvent
from server.exc import ExceptionResponse
from typing import List
from ._model import Model


class ModelEvent(Model):
    def create_one(self, title: str, desc: str, time_begin: datetime, time_end: datetime) -> TableEvent:
        event = TableEvent(title, desc, time_begin, time_end)
        self.session.add(event)
        self.session.commit()
        self.session.refresh(event)
        return event

    def del_by_uuid(self, uuid: str):
        row = self.session.query(TableEvent).filter(TableEvent.uuid == uuid).delete()
        if row <= 0:
            raise ExceptionResponse(404, "Not found")
        return row

    def find_all(self) -> List[TableEvent]:
        return self.session.query(TableEvent).all()
