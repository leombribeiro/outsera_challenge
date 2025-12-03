import pytest_asyncio
from httpx import AsyncClient, ASGITransport
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from src.outsera_challenge.main import app
from src.outsera_challenge.db.models import Base, Movie
from src.outsera_challenge.db.db import get_session


TEST_DATABASE_URL = "sqlite+aiosqlite:///:memory:"


@pytest_asyncio.fixture
async def test_engine():
    engine = create_async_engine(TEST_DATABASE_URL, echo=False)

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield engine

    await engine.dispose()


@pytest_asyncio.fixture
async def test_session(test_engine):
    SessionLocal = async_sessionmaker(
        bind=test_engine, class_=AsyncSession, expire_on_commit=False
    )

    async with SessionLocal() as session:
        yield session


@pytest_asyncio.fixture
async def seed_database(test_engine):
    SessionLocal = async_sessionmaker(
        bind=test_engine, class_=AsyncSession, expire_on_commit=False
    )

    async with SessionLocal() as session:
        movies = [
            Movie(
                id="some_id_1",
                year=2008,
                title="Some Movie 1",
                studios="Studio 1",
                producers="Producer 1",
                winner=True,
            ),
            Movie(
                id="some_id_2",
                year=2009,
                title="Some Movie 2",
                studios="Studio 1",
                producers="Producer 1",
                winner=True,
            ),
            Movie(
                id="some_id_3",
                year=2018,
                title="Some Movie 2",
                studios="Studio 2",
                producers="Producer 2",
                winner=True,
            ),
            Movie(
                id="some_id_4",
                year=2019,
                title="Some Movie 3",
                studios="Studio 2",
                producers="Producer 2",
                winner=True,
            ),
            Movie(
                id="some_id_6",
                year=1900,
                title="Some Movie 1",
                studios="Studio 1",
                producers="Producer 3",
                winner=True,
            ),
            Movie(
                id="some_id_7",
                year=1999,
                title="Some Movie 2",
                studios="Studio 1",
                producers="Producer 3",
                winner=True,
            ),
            Movie(
                id="some_id_8",
                year=2000,
                title="Some Movie 2",
                studios="Studio 2",
                producers="Producer 4",
                winner=True,
            ),
            Movie(
                id="some_id_9",
                year=2099,
                title="Some Movie 3",
                studios="Studio 2",
                producers="Producer 4",
                winner=True,
            ),
        ]

        for movie in movies:
            session.add(movie)

        await session.commit()


@pytest_asyncio.fixture
async def client(test_engine, seed_database):
    async def override_get_session():
        SessionLocal = async_sessionmaker(
            bind=test_engine, class_=AsyncSession, expire_on_commit=False
        )
        async with SessionLocal() as session:
            yield session

    app.dependency_overrides[get_session] = override_get_session

    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        yield ac

    app.dependency_overrides.clear()


@pytest_asyncio.fixture
async def client_empty(test_engine):
    async def override_get_session():
        SessionLocal = async_sessionmaker(
            bind=test_engine, class_=AsyncSession, expire_on_commit=False
        )
        async with SessionLocal() as session:
            yield session

    app.dependency_overrides[get_session] = override_get_session

    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        yield ac

    app.dependency_overrides.clear()
