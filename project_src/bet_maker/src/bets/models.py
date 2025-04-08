import enum
from datetime import datetime

from sqlalchemy import DateTime, DECIMAL, Enum, text
from sqlalchemy.orm import Mapped, mapped_column

from src.core.database import Base


class EventState(enum.Enum):
    NEW = 1
    FINISHED_WIN = 2
    FINISHED_LOSE = 3


class Bet(Base):
    __tablename__ = "bets"

    bet_id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )
    event_id: Mapped[int] = mapped_column(
        nullable=False,
    )
    event_state: Mapped[EventState] = mapped_column(
        Enum(EventState),
        default=EventState.NEW,
        nullable=True,
    )
    amount: Mapped[float] = mapped_column(
        DECIMAL(8, 2),
        nullable=False,
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        server_default=text("TIMEZONE('utc', now())"),
    )
