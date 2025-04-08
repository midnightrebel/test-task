import enum
from datetime import datetime

from sqlalchemy import DateTime, DECIMAL, Enum, String
from sqlalchemy.orm import Mapped, mapped_column

from src.core.database import Base


class EventState(enum.Enum):
    NEW = 1
    FINISHED_WIN = 2
    FINISHED_LOSE = 3


class Event(Base):
    __tablename__ = "events"

    event_id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )
    event_title: Mapped[str] = mapped_column(String(100), nullable=False)
    coefficient: Mapped[float] = mapped_column(
        DECIMAL(8, 2),
        nullable=False,
    )
    deadline: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
    )
    state: Mapped[EventState] = mapped_column(
        Enum(EventState),
        default=EventState.NEW,
        nullable=False,
    )
