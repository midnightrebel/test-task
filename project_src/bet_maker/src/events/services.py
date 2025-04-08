import aiohttp

from src.core.exception import BaseHTTPException
from src.events.exceptions import EventNotFound


class EventCommunicateService:
    async def get_all_active(self):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get("http://line_provider:8000/line-provider/events/") as response:
                    response.raise_for_status()
                    return await response.json()
        except Exception as e:
            raise BaseHTTPException from e

    async def get_one(self, event_id: int):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f"http://line_provider:8000/line-provider/events/{event_id}") as response:
                    response.raise_for_status()
                    return await response.json()
        except aiohttp.ClientResponseError as e:
            raise EventNotFound from e
        except Exception as e:
            raise BaseHTTPException from e