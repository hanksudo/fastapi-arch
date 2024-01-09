from contextlib import asynccontextmanager

from fastapi import FastAPI
from app.internal import routers
from app.internal.core.scheduler import Scheduler
from app.internal.core.seeder import Seeder
from app.internal.deps import databaseManager


@asynccontextmanager
async def lifespan(app: FastAPI):
    databaseManager.init_db()

    with databaseManager.session() as db:
        Seeder(db).seed()
        Scheduler(db).start()
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(routers.api)
app.include_router(routers.websocket)
