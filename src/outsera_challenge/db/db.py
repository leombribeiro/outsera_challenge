from sqlalchemy.ext.asyncio import (
    AsyncSession,
    AsyncEngine,
    create_async_engine,
    async_sessionmaker,
)

from fastapi import Depends
from typing import Annotated

engine: AsyncEngine | None = None


def get_engine():
    global engine
    if engine is None:
        engine = create_async_engine("sqlite+aiosqlite:///./movies.db")
    return engine


async def session():
    session = async_sessionmaker(bind=get_engine())
    yield session()


Session = Annotated[AsyncSession, Depends(session)]
