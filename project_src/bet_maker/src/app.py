import asyncio
from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.bets.routers import router as router_bets
from src.core.event_consumer import consumer_run
from src.events.routers import router as router_events


@asynccontextmanager
async def event_consumer_lifespan(app: FastAPI):
    current_loop = asyncio.get_event_loop()
    rabbit_task = current_loop.create_task(consumer_run())
    try:
        yield
    finally:
        if not rabbit_task.done():
            rabbit_task.cancel()
            try:
                await rabbit_task
            except asyncio.CancelledError:
                pass

app = FastAPI(
    version="0.0.1",
    root_path="/bet-maker",
    lifespan=event_consumer_lifespan,
)

app.include_router(router_events)
app.include_router(router_bets)
