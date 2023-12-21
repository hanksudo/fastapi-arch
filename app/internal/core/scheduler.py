import asyncio

from apscheduler.executors.asyncio import AsyncIOExecutor  # type: ignore
from apscheduler.executors.pool import ThreadPoolExecutor  # type: ignore
from apscheduler.schedulers.background import BackgroundScheduler  # type: ignore
from internal import deps, schemas, usecases
from sqlalchemy.orm import Session


class Scheduler:
    def __init__(self, db: Session):
        self.db = db

    def start(self):
        job_defaults = {"coalesce": True, "max_instances": 1}
        executors = {"default": ThreadPoolExecutor(), "asyncio": AsyncIOExecutor()}
        scheduler = BackgroundScheduler(
            timezone="Asia/Tokyo", job_defaults=job_defaults, executors=executors
        )

        scheduler._eventloop = asyncio.get_event_loop()
        scheduler.add_job(self._run, "interval", seconds=10)  # type: ignore
        scheduler.add_job(self._send_message, "interval", seconds=3, executor="asyncio")  # type: ignore
        scheduler.start()  # type: ignore

    def _run(self):
        print("Scheduler running...")
        robot = usecases.robot.get_robot(self.db, 1)
        if robot:
            print(robot.id)
            print(schemas.RobotResponse.model_validate(robot))

    async def _send_message(self):
        await deps.notifier.broadcast_message("test from scheduler")
