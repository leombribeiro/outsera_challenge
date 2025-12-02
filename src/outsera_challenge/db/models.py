from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase


class Base(DeclarativeBase):
    pass


class Movie(Base):
    __tablename__ = "movies"

    id: Mapped[int] = mapped_column(primary_key=True)
    year: Mapped[int] = mapped_column(nullable=False)
    title: Mapped[str] = mapped_column(nullable=False)
    studios: Mapped[str] = mapped_column(nullable=False)
    producers: Mapped[str] = mapped_column(nullable=False)
    winner: Mapped[bool] = mapped_column(nullable=False)
