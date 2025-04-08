from datetime import datetime, timezone
from typing import Optional

from pydantic import BaseModel, Field, field_serializer

from src.core.config import settings
from src.events.models import EventState


class EventIDSchema(BaseModel):
    event_id: int


class EventStateSchema(BaseModel):
    state: EventState = Field(..., description="Event status")

    class Config:
        from_attributes = True


class EventCreateSchema(BaseModel):
    event_title: str
    coefficient: float  = Field(ge=0)
    deadline: datetime = Field(
        ...,
        example=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M"),
    )

    @field_serializer("deadline", when_used="json")
    def serialize_format_deadline(self, deadline: datetime):
        return deadline.strftime("%Y-%m-%d %H:%M")

    class Config:
        from_attributes = True


class EventUpdateSchema(EventStateSchema, EventIDSchema):
    event_title: Optional[str]
    coefficient: Optional[float]
    deadline: Optional[datetime] = Field(
        None,
        example=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M"),
    )

    @field_serializer("deadline", when_used="json")
    def serialize_format_deadline(self, deadline: datetime):
        return deadline.strftime("%Y-%m-%d %H:%M")

    class Config:
        from_attributes = True


class EventSchema(EventStateSchema, EventCreateSchema, EventIDSchema):
    class Config:
        from_attributes = True
