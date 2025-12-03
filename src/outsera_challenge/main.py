from contextlib import asynccontextmanager
from typing import Annotated

from fastapi import Depends, FastAPI

from src.outsera_challenge.csv import CSVReader
from src.outsera_challenge.models.movie import WinnerResponse
from src.outsera_challenge.services.movie_service import MovieService


@asynccontextmanager
async def lifespan(app: FastAPI):
    await CSVReader.import_csv()
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/winners")
async def get_winners(
    movie_service: Annotated[MovieService, Depends()],
) -> WinnerResponse:
    return await movie_service.get_winners()
