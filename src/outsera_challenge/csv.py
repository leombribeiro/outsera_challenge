import csv
from src.outsera_challenge.models.movie import MovieModel
from src.outsera_challenge.services.movie_service import MovieService
from src.outsera_challenge.repositories.movie_repository import MovieRepository
from src.outsera_challenge.db.db import session


class CSVReader:
    @staticmethod
    async def import_csv():
        session_db = session()
        db = await session_db.__anext__()

        try:
            movie_repository = MovieRepository(db)
            movie_service = MovieService(movie_repository)
            with open("movielist.csv", "r", encoding="utf-8") as csv_file:
                reader = csv.DictReader(csv_file, delimiter=";")
                for row in reader:
                    producer = row.get("producers", None)
                    if producer is None:
                        continue

                    movie = MovieModel(
                        year=int(row.get("year")),
                        title=row.get("title"),
                        studios=row.get("studios"),
                        producers=row.get("producers", None),
                        winner=row.get("winner", False) == "yes",
                    )

                    await movie_service.create_movie(movie)

        finally:
            await db.aclose()
