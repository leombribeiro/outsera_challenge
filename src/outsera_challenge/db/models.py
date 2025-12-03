from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy import Boolean


class Base(DeclarativeBase):
    pass


class Movie(Base):
    __tablename__ = "movies"

    id: Mapped[str] = mapped_column(primary_key=True)
    year: Mapped[int] = mapped_column()
    title: Mapped[str] = mapped_column()
    studios: Mapped[str] = mapped_column()
    producers: Mapped[str] = mapped_column(nullable=True)
    winner: Mapped[bool] = mapped_column(Boolean, default=False)
