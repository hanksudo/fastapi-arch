from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .base import BaseDatabaseModel


class Robot(BaseDatabaseModel):
    __tablename__ = "robot"

    name: Mapped[str] = mapped_column(String(256), nullable=False, unique=True)
