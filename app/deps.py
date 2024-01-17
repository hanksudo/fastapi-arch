from contextlib import AbstractContextManager
from collections.abc import Callable

from app.infrastructure.database import DatabaseManager
from app.infrastructure.notifier import Notifier

from app.internal.core import environment
from app.internal.usecases import RobotUseCase
from app.internal.repositories import RobotRepository
from app.internal.models import Robot

from sqlalchemy.orm import Session

class DatabaseProvider:
    def __init__(self, *, session_factory: Callable[..., AbstractContextManager[Session]]) -> None:
        self.session_factory = session_factory

    def NewRobotRepository(self) -> RobotRepository:
        return RobotRepository(Robot, self.session_factory)

class UsecaseProvider:
    def __init__(self, database_provider: DatabaseProvider):
        self.database_provider = database_provider

    def NewRobotUseCase(self) -> RobotUseCase:
        return RobotUseCase(self.database_provider.NewRobotRepository())


databaseManager = DatabaseManager(environment.DATABASE_URL)
usecase_provider = UsecaseProvider(DatabaseProvider(session_factory=databaseManager.session))
notifier = Notifier()