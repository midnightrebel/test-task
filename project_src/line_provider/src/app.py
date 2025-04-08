from fastapi import FastAPI

from src.events.routers import router as router_events


app = FastAPI(
    root_path="/line-provider",
)

app.include_router(router_events)
