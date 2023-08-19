from datetime import datetime
from typing import Optional

from pydantic import AfterValidator, BaseModel
from typing_extensions import Annotated

from src.recurring_event.models import IntervalTypes

IntervalTypeToStr = Annotated[Optional[IntervalTypes], AfterValidator(lambda x: x.value)]


class RecurringEventData(BaseModel):
    id: int
    title: str
    start: Optional[datetime] = None
    interval: Optional[IntervalTypes] = IntervalTypes.DAY
    interval_count: Optional[int] = 1
    description: Optional[str]

    class Config:
        from_attributes = True


class RecurringEventDataCreate(BaseModel):
    title: str
    start: Optional[datetime] = None
    interval: IntervalTypeToStr = IntervalTypes.DAY
    interval_count: Optional[int] = 1
    description: Optional[str]
