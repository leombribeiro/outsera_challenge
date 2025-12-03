from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

engine: AsyncEngine | None = None


def get_engine():
    global engine
    if engine is None:
        engine = create_async_engine("sqlite+aiosqlite:///./movies.db")
    return engine


async def get_session():
    SessionLocal = async_sessionmaker(
        bind=get_engine(),
        class_=AsyncSession,
    )
    async with SessionLocal() as session:
        yield session


Session = Annotated[AsyncSession, Depends(get_session)]
