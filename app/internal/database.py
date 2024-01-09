from collections.abc import Generator
from contextlib import contextmanager
from logging import getLogger

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, scoped_session, sessionmaker

logger = getLogger("uvicorn.app")

class Base(DeclarativeBase):
    pass

class DatabaseManager:
    def __init__(self, db_url: str) -> None:
        self._engine = create_engine(db_url, echo=False)
        self._session_factory = scoped_session(
            sessionmaker(autocommit=False, autoflush=False, bind=self._engine)
        )

    def init_db(self) -> None:
        Base.metadata.create_all(bind=self._engine)

    @contextmanager
    def session(self) -> Generator[Session, None, None]:
        session = self._session_factory()
        try:
            yield session
        except Exception as e:
            session.rollback()
            logger.error(f"sqlalchemy error: {e}")
            # raise
        finally:
            session.close()