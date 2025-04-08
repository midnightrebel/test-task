from fastapi import APIRouter

from src.bets.exceptions import BetCannotBePlace
from src.bets.schemas import BetCreateSchema, BetSchema, BetUpdateSchema
from src.bets.services import BetService
from typing import List

router = APIRouter(
    tags=["Bets"],
)


@router.get("/bets", response_model=List[BetSchema])
async def get_bets():
    "All bets history"

    return await BetService.get_all()



@router.post("/bet", response_model=BetSchema)
async def bet_event(bet: BetCreateSchema):
    "Bet by event ID"

    new_bet = await BetService.place_bet_event(bet)
    if not new_bet:
        raise BetCannotBePlace

    return new_bet
