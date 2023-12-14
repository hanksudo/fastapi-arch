from typing import Annotated

from fastapi import Depends
from infra.database import DatabaseManager
from infra.notifier import Notifier
from sqlalchemy.orm import Session

from app.core import config

database = DatabaseManager(config.DATABASE_URL)
notifier = Notifier()

DatabaseDep = Annotated[Session, Depends(database.get_db_deps)]
