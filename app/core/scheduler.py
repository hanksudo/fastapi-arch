from apscheduler.schedulers.background import BackgroundScheduler  # type: ignore
from sqlalchemy.orm import Session

from app import schemas, usecases


class Scheduler:
    def __init__(self, db: Session):
        self.db = db

    def start(self):
        scheduler = BackgroundScheduler()
        scheduler.add_job(self._run, "interval", seconds=1)  # type: ignore
        scheduler.start()  # type: ignore

    def _run(self):
        print("Scheduler running...")
        robot = usecases.robot.get_robot(self.db, 1)
        if robot:
            print(robot.id)
            print(schemas.RobotResponse.model_validate(robot))
