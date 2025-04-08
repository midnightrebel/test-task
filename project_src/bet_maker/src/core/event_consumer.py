import asyncio
import json

from aio_pika import IncomingMessage

from src.core.rabbitmq import async_rabbitmq_connection
from src.tasks.bet_tasks import update_completed_event_state


async def handle_message(message: IncomingMessage):
    try:
        data = message.body.decode("utf-8")
        data: dict = json.loads(data)

        update_completed_event_state.delay(
            data.get("event_id"), data.get("state")
        )

        await message.ack()
    except Exception as e:
        print(f"Error handling message: {e}")
        await message.nack(requeue=True)


async def consumer_run():
    async with async_rabbitmq_connection as (_, queue):
        async with queue.iterator() as queue_iter:
            async for message in queue_iter:
                await handle_message(message)


if __name__ == "__main__":
    asyncio.run(consumer_run())
