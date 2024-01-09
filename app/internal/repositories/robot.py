from app.internal import models, schemas

from .base import BaseRepository


class RobotRepository(
    BaseRepository[models.Robot, schemas.RobotCreate, schemas.RobotUpdate]
):
    def list_by(self, name: str) -> list[models.Robot]:
        with self.session_factory() as session:
            return session.query(self.model).filter(self.model.name == name).all()