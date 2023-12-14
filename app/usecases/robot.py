from sqlalchemy.orm import Session

from app import cruds, models


def get_robot(db: Session, id: int) -> models.Robot | None:
    return cruds.robot.get(db, id)
