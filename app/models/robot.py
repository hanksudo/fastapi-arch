from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .base import BaseModel


class Robot(BaseModel):
    __tablename__ = "robot"

    name: Mapped[str] = mapped_column(String(256), nullable=False, unique=True)
