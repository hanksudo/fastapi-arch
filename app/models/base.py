from infra.database import Base
from sqlalchemy import Column, Integer
from sqlalchemy.dialects.sqlite import TIMESTAMP as Timestamp
from sqlalchemy.sql import func


class BaseModel(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(Timestamp, nullable=False, server_default=func.now())
    updated_at = Column(
        Timestamp, nullable=False, server_default=func.now(), onupdate=func.now()
    )
