from apscheduler.schedulers.asyncio import AsyncIOScheduler  # type: ignore

from app import deps
from sqlalchemy.orm import Session
from logging import getLogger

logger = getLogger("uvicorn.app")

class Scheduler:
    def __init__(self, db: Session):
        self.db = db

    def start(self):
        job_defaults = {"coalesce": True, "max_instances": 1}
        scheduler = AsyncIOScheduler(timezone="Asia/Tokyo", job_defaults=job_defaults)

        scheduler.add_job(self._run, "interval", seconds=10)  # type: ignore
        scheduler.add_job(self._send_message, "interval", seconds=3)  # type: ignore
        scheduler.start()  # type: ignore

    def _run(self):
        robot = deps.usecase_provider.NewRobotUseCase().get_robot(1)
        if robot is not None:
            logger.info(f"Scheduler (10s): {robot.id}")

    async def _send_message(self):
        await deps.notifier.broadcast_message("test from scheduler")
