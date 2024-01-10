from datetime import datetime
from sqlalchemy import Integer
from sqlalchemy.dialects.mysql import TIMESTAMP as Timestamp
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func
from app.infrastructure.database import Base

class BaseDatabaseModel(Base):
    __abstract__ = True

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    created_at: Mapped[datetime] = mapped_column(Timestamp, nullable=False, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        Timestamp, nullable=False, server_default=func.now(), onupdate=func.now()
    )
