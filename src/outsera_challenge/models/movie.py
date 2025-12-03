from pydantic import BaseModel, Field


class MovieModel(BaseModel):
    year: int
    title: str
    studios: str
    producers: str | None = None
    winner: bool = False


class MovieFilter(BaseModel):
    winner: bool | None = None


class MovieInterval(BaseModel):
    producer: str
    interval: int
    previous_win: int = Field(serialization_alias="previousWin")
    following_win: int = Field(serialization_alias="followingWin")


class WinnerResponse(BaseModel):
    min: list[MovieInterval]
    max: list[MovieInterval]
