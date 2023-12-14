from fastapi import APIRouter

from app import schemas, usecases

router = APIRouter()


@router.get("/{robot_id}")
async def get_robot(robot_id: int) -> schemas.RobotResponse:
    return usecases.get_robot(id=robot_id)
