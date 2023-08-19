from fastapi import APIRouter

from src.recurring_event.models import RecurringEvent
from src.recurring_event.serializer import RecurringEventData, RecurringEventDataCreate

router = APIRouter(prefix="/api")


@router.post("/events/", response_model=RecurringEventData)
async def create_event(event_data: RecurringEventDataCreate):
    event = RecurringEvent(**event_data.model_dump(exclude_unset=True))
    event.flush()
    return RecurringEventData.model_validate(RecurringEvent[event.id])
