from fastapi import APIRouter, Depends
from infra.database import get_db

# from app import deps
from app.routers.api import robot

api_router = APIRouter(dependencies=[Depends(get_db)])
api_router.include_router(robot.router, prefix="/robot")
