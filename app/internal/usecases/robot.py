from internal import repositories, models
from sqlalchemy.orm import Session


def get_robot(db: Session, id: int) -> models.Robot | None:
    return repositories.robot.get(db, id)
