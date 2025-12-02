from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine, async_sessionmaker
from sqlalchemy.orm import Annotated, AsyncSession
from fastapi import Depends

engine: AsyncEngine | None = None


def get_engine():
    global engine
    if engine is None:
        engine = create_async_engine("sqlite:///./movies.db")
    return engine


async def session():
    session = async_sessionmaker(bind=get_engine())
    try:
        yield session()
    finally:
        session.close()


Session = Annotated[AsyncSession, Depends(session)]
