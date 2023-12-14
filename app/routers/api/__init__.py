from fastapi import APIRouter

from app.routers.api import robot

api_router = APIRouter()
api_router.include_router(robot.router, prefix="/robots")
