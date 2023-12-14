from collections.abc import Generator
from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, scoped_session, sessionmaker


class Base(DeclarativeBase):
    pass


class DatabaseManager:
    def __init__(self, db_url: str) -> None:
        self._engine = create_engine(db_url, echo=True)
        self._session_factory = scoped_session(
            sessionmaker(autocommit=False, autoflush=False, bind=self._engine)
        )

    def init_db(self) -> None:
        Base.metadata.create_all(bind=self._engine)

    @contextmanager
    def get_db(self) -> Generator[Session, None, None]:
        db = self._session_factory()
        try:
            yield db
        except Exception:
            db.rollback()
            raise
        finally:
            db.close()

    def get_db_deps(self) -> Generator[Session, None, None]:
        with self.get_db() as db:
            yield db
