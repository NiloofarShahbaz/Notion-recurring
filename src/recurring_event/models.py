from enum import Enum

from tortoise import fields
from tortoise.models import Model


class IntervalTypes(Enum):
    DAY = "DAY"
    WEEK = "WEEK"
    MONTH = "MONTH"
    YEAR = "YEAR"


class RecurringEvent(Model):
    id = fields.IntField(pk=True)
    title = fields.TextField()
    start = fields.DatetimeField(auto_now_add=True)
    interval = fields.CharEnumField(enum_type=IntervalTypes, max_length=5, default=IntervalTypes.DAY)
    interval_count = fields.SmallIntField()
    description = fields.TextField()

    def __str__(self):
        return self.title
