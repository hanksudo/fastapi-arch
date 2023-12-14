from infra.database import Base
from sqlalchemy import Column, Field, text
from sqlalchemy.dialects.sqlite import TIMESTAMP as Timestamp


class BaseModel(Base):
    id: int | None = Field(default=None, primary_key=True)
    created_at = Column(
        Timestamp, nullable=False, server_default=text("current_timestamp")
    )
    updated_at = Column(
        Timestamp,
        nullable=False,
        server_default=text("current_timestamp on update current_timestamp"),
    )
