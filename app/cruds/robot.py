from app import models, schemas

from .base import CRUDBase


class CRUDRobot(CRUDBase[models.Robot, schemas.RobotCreate, schemas.RobotUpdate]):
    pass


robot = CRUDRobot(models.Robot)
