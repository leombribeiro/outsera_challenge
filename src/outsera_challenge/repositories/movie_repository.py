from uuid import uuid4

from sqlalchemy import select

from src.outsera_challenge.db.base_repository import BaseRepository
from src.outsera_challenge.db.models import Movie
from src.outsera_challenge.models.movie import MovieFilter, MovieModel


class MovieRepository(BaseRepository):
    async def create_movie(self, movie_data: MovieModel) -> None:
        movie = Movie(**movie_data.dict(), id=str(uuid4()))
        self.session.add(movie)
        await self.session.commit()

    async def get_movies(self, filter: MovieFilter) -> list[Movie]:
        stmt = select(Movie)

        if filter.winner is not None:
            stmt = stmt.filter(Movie.winner == filter.winner)

        stmt = stmt.order_by(Movie.year)
        result = await self.session.execute(stmt)

        return result.scalars().all()
