from contextlib import asynccontextmanager

from fastapi import FastAPI
from internal import routers
from internal.core import Scheduler, Seeder
from internal.deps import database
from internal.models import Base


@asynccontextmanager
async def lifespan(app: FastAPI):
    database.init_db(Base)

    with database.get_db() as db:
        Seeder(db).seed()
        Scheduler(db).start()
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(routers.api)
app.include_router(routers.websocket)
