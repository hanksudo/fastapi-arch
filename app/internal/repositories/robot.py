from internal import models, schemas

from .base import BaseRepository


class RobotRepository(
    BaseRepository[models.Robot, schemas.RobotCreate, schemas.RobotUpdate]
):
    pass


robot = RobotRepository(models.Robot)
