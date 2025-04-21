from sqlalchemy import select, insert
from src.models import UrlModel
from src.database import Base, async_engine, new_async_session


class AsyncCRUD:
    @staticmethod
    async def create_tables():
        async with async_engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)

    @staticmethod
    async def insert_urls(short_url: str, long_url: str):
        async with new_async_session() as session:
            url = UrlModel(short_url=short_url, long_url=long_url)
            session.add(url)
            await session.commit()

    @staticmethod
    async def select_urls(short_url: str):
        async with new_async_session() as session:
            query = select(UrlModel).filter_by(short_url=short_url)
            result = await session.execute(query)
            url = result.scalars().one_or_none()
            return url.long_url
