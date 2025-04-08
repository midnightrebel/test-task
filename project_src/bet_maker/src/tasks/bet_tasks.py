import asyncio

from src.bets.schemas import BetIDSchema, BetStateSchema, BetUpdateSchema
from src.bets.services import BetService
from src.core.celery import celery_app
from src.events.schemas import EventIDSchema, EventStateSchema


@celery_app.task
def update_completed_event_state(
    event_id: EventIDSchema, event_state: EventStateSchema
):
    """The task for update completed event state"""

    current_loop = asyncio.get_event_loop()
    current_loop.run_until_complete(
        update_completed_event_state_async(event_id, event_state)
    )


async def update_completed_event_state_async(
    event_id: EventIDSchema, event_state: EventStateSchema
):
    bets_id = await BetService.get_bets_with_event_id(event_id=event_id)

    for bet_id in bets_id:
        await BetService.update_bet(
            BetUpdateSchema(
                **{
                    "bet_id": bet_id,
                    "event_state": event_state,
                }
            )
        )
