from fastapi import APIRouter

# from src.recurring_event.models import RecurringEvent

router = APIRouter(prefix="/api")

#
# @router.post("/events/", response_model=RecurringEventReadModel)
# async def create_event(event_data: RecurringEventCreateModel):
#     print(event_data)
#     event = await RecurringEvent.create(**event_data.dict(exclude_unset=True))
#     return await RecurringEventReadModel.from_tortoise_orm(event)
#
#
# @router.get("/events/", response_model=list[RecurringEventReadModel])
# async def get_events():
#     print(await RecurringEvent.all().values('id', 'interval'))
#     return await RecurringEventReadModel.from_queryset(RecurringEvent.all())
#
#
# @router.get("/events/{event_id}/", response_model=RecurringEventReadModel)
# async def get_event(event_id: int):
#     return await RecurringEventReadModel.from_queryset_single(RecurringEvent.get(id=event_id))
