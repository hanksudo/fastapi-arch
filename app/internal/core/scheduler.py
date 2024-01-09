import asyncio

from apscheduler.executors.asyncio import AsyncIOExecutor  # type: ignore
from apscheduler.executors.pool import ThreadPoolExecutor  # type: ignore
from apscheduler.schedulers.background import BackgroundScheduler  # type: ignore
from app.internal.deps import provider, notifier
from sqlalchemy.orm import Session
from logging import getLogger

logger = getLogger("uvicorn.app")

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
        robot = provider.NewRobotUseCase().get_robot(1)
        if robot is not None:
            logger.info(f"Scheduler (10s): {robot.id}")

    async def _send_message(self):
        await notifier.broadcast_message("test from scheduler")
