import aio_pika

from src.core.config import overall_settings


class AsyncRabbitMQConnection:
    def __init__(
        self,
        url: str,
        exchange_name: str,
        exchange_type: aio_pika.ExchangeType,
        queue_name: str,
    ):
        self.url = url
        self.exchange_name = exchange_name
        self.exchange_type = exchange_type
        self.queue_name = queue_name
        self.connection: aio_pika.RobustConnection = None
        self.channel: aio_pika.RobustChannel = None
        self.exchange: aio_pika.RobustExchange = None
        self.queue: aio_pika.RobustQueue = None

    async def __aenter__(self):
        self.connection = await aio_pika.connect_robust(self.url)

        self.channel = await self.connection.channel()

        self.exchange = await self.channel.declare_exchange(
            name=self.exchange_name,
            type=self.exchange_type,
            durable=True,
        )
        self.queue = await self.channel.declare_queue(
            name=self.queue_name,
            durable=True,
        )

        await self.queue.bind(
            exchange=self.exchange,
            routing_key=self.queue.name,
        )

        return self.exchange, self.queue

    async def __aexit__(self, exc_type, exc_value, traceback):
        if self.channel and not self.channel.is_closed:
            await self.channel.close()
        if self.connection and not self.connection.is_closed:
            await self.connection.close()


async_rabbitmq_connection = AsyncRabbitMQConnection(
    url=overall_settings.RABBITMQ_URL,
    exchange_name=overall_settings.RABBITMQ_EXCHANGE,
    exchange_type=overall_settings.RABBITMQ_EXCHANGE_TYPE,
    queue_name=overall_settings.RABBITMQ_CELERY_EVENT_STATE_QUEUE,
)
