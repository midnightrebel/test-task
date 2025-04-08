from sqlalchemy import select

from src.core.database import async_session_maker


class BaseService:
    model = None

    @classmethod
    async def get_one(cls, *args, **kwargs):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(*args, **kwargs)
            result = await session.execute(query)

            return result.scalar_one_or_none()

    @classmethod
    async def get_all(cls, *args, **kwargs):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(*args, **kwargs)
            result = await session.execute(query)

            return result.scalars().all()
