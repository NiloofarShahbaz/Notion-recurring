from datetime import datetime
from enum import Enum

from pony import orm

from src.server import db


class IntervalTypes(Enum):
    DAY = "DAY"
    WEEK = "WEEK"
    MONTH = "MONTH"
    YEAR = "YEAR"


class RecurringEvent(db.Entity):
    id = orm.PrimaryKey(int, auto=True)
    title = orm.Required(str)
    start = orm.Required(datetime, default=datetime.now)
    interval = orm.Required(str, default=IntervalTypes.DAY, py_check=lambda x: x in IntervalTypes)
    interval_count = orm.Required(int, default=1)
    description = orm.Optional(str)

    def __str__(self):
        return self.id
