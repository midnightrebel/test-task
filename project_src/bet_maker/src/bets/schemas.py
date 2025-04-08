from datetime import datetime, timezone
from typing import Optional

from pydantic import BaseModel, Field, field_serializer

from src.bets.models import EventState


class BetIDSchema(BaseModel):
    bet_id: int


class BetStateSchema(BaseModel):
    event_state: EventState

    class Config:
        from_attributes = True


class BetCreateSchema(BaseModel):
    event_id: int
    amount: float

    class Config:
        from_attributes = True


class BetUpdateSchema(BetStateSchema, BetIDSchema):
    event_state: Optional[EventState]
    amount: Optional[float]

    class Config:
        from_attributes = True


class BetSchema(BetCreateSchema, BetStateSchema, BetIDSchema):
    created_at: datetime = Field(
        ...,
        example=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M"),
    )

    @field_serializer("created_at", when_used="json")
    def serialize_format_datetime(self, deadline: datetime):
        return deadline.strftime("%Y-%m-%d %H:%M")

    class Config:
        from_attributes = True
