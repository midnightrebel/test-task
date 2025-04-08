from fastapi import APIRouter

from typing import List

from src.events.schemas import EventSchema
from src.events.services import EventCommunicateService

router = APIRouter(
    prefix="/events",
    tags=["Events"],
)

bet_event_service = EventCommunicateService()


@router.get("/")
async def get_events() -> List[EventSchema]:
    "Get all active events"

    return await bet_event_service.get_all_active()