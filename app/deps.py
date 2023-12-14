from typing import Annotated

from fastapi import Depends
from infra.database import DatabaseManager
from sqlalchemy.orm import Session

from app.core import config

database = DatabaseManager(config.DATABASE_URL)

DatabaseDep = Annotated[Session, Depends(database.get_db_deps)]
