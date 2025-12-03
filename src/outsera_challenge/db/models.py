from sqlalchemy import Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


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
