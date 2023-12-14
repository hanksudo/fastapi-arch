from app import models, schemas

from .base import BaseCRUD


class RobotCRUD(BaseCRUD[models.Robot, schemas.RobotCreate, schemas.RobotUpdate]):
    pass


robot = RobotCRUD(models.Robot)
