from fastapi import APIRouter

from src.events.exceptions import (
    EventCannotBeAdded,
    EventCannotBeUpdated,
    EventNotFound,
)
from src.events.schemas import EventCreateSchema, EventSchema, EventUpdateSchema
from src.events.services import EventService
from typing import List

router = APIRouter(
    prefix="/events",
    tags=["Events"],
)


@router.get("/")
async def get_events() -> List[EventSchema]:
    "Get all active events"

    return await EventService.get_all_active()


@router.get("/{event_id}/")
async def get_event(event_id: int) -> EventSchema:
    "Get an event by ID"

    event = await EventService.get_one(event_id=event_id)
    if not event:
        raise EventNotFound

    return event


@router.post("/create/")
async def create_event(event: EventCreateSchema) -> EventSchema:
    "Create new event"

    new_event = await EventService.create_event(event)
    if not new_event:
        raise EventCannotBeAdded

    return new_event

