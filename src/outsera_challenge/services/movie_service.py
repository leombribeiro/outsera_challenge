from typing import Annotated
from itertools import pairwise
from fastapi import Depends
from collections import defaultdict
from src.outsera_challenge.utils import Utils
from src.outsera_challenge.models.movie import (
    MovieModel,
    MovieFilter,
    WinnerResponse,
    MovieInterval,
)
from src.outsera_challenge.repositories.movie_repository import MovieRepository


class MovieService:
    def __init__(self, movie_repository: Annotated[MovieRepository, Depends()]):
        self.movie_repository = movie_repository

    async def create_movie(self, movie_data: MovieModel) -> None:
        await self.movie_repository.create_movie(movie_data)

    async def get_winners(self) -> WinnerResponse:
        movies = await self.movie_repository.get_movies(
            filter=MovieFilter(winner=True),
        )

        winners = defaultdict(list)
        for movie in movies:
            for producer in Utils.split_names(movie.producers):
                winners[producer].append(movie.year)

        intervals = self._get_intervals(winners)
        if not intervals:
            return WinnerResponse(min=[], max=[])

        min_intervals, max_intervals = self._get_min_max_intervals(intervals)

        return WinnerResponse(
            min=min_intervals,
            max=max_intervals,
        )

    def _get_intervals(self, winners: dict) -> list[MovieInterval]:
        return [
            MovieInterval(
                producer=producer,
                interval=year_following - year_previous,
                previous_win=year_previous,
                following_win=year_following,
            )
            for producer, years in winners.items()
            if len(years) > 1
            for year_previous, year_following in pairwise(years)
        ]

    def _get_min_max_intervals(
        self, intervals: list[MovieInterval]
    ) -> tuple[list[MovieInterval], list[MovieInterval]]:
        min_value = min(intervals, key=lambda interval: interval.interval)
        max_value = max(intervals, key=lambda interval: interval.interval)

        min_intervals = []
        max_intervals = []

        for interval in intervals:
            if interval.interval == min_value.interval:
                min_intervals.append(interval)
            if interval.interval == max_value.interval:
                max_intervals.append(interval)

        return min_intervals, max_intervals
