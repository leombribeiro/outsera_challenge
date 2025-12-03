from src.outsera_challenge.db.db import Session


class BaseRepository:
    def __init__(self, session: Session):
        self.session = session
