from typing import Annotated

from fastapi import Depends
from infrastructure.database import DatabaseManager
from infrastructure.notifier import Notifier
from internal.core import config
from sqlalchemy.orm import Session

database = DatabaseManager(config.DATABASE_URL)
notifier = Notifier()

DatabaseDep = Annotated[Session, Depends(database.get_db_deps)]
