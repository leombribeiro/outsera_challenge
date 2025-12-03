from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends
from typing import Annotated

from src.outsera_challenge.services.movie_service import MovieService


from src.outsera_challenge.models.movie import WinnerResponse
from src.outsera_challenge.csv import CSVReader


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
