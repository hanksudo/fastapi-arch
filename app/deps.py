from contextlib import AbstractContextManager
from typing import Callable

from app.infrastructure.notifier import Notifier

from app.internal.core import config
from app.internal.database import DatabaseManager
from app.internal.usecases import RobotUseCase
from app.internal.repositories import RobotRepository
from app.internal.models import Robot

from sqlalchemy.orm import Session

class Provider:
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]):
        self.session_factory = session_factory

    def NewRobotUseCase(self) -> RobotUseCase:
        return RobotUseCase(RobotRepository(Robot, self.session_factory))


databaseManager = DatabaseManager(config.DATABASE_URL)
provider = Provider(databaseManager.session)
notifier = Notifier()