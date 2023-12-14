from internal import cruds, models
from sqlalchemy.orm import Session


def get_robot(db: Session, id: int) -> models.Robot | None:
    return cruds.robot.get(db, id)
