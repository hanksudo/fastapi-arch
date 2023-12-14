from contextlib import asynccontextmanager

from fastapi import FastAPI
from infra.database import init_db

from app import routers
from app.core import seed


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    seed.seed()
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(routers.api)
# app.include_router(routers.websocket)
