from fastapi import APIRouter, HTTPException

from app import deps, schemas, usecases

router = APIRouter()


@router.get("/{robot_id}", response_model=schemas.RobotResponse)
async def get_robot(robot_id: int, db: deps.DatabaseDep) -> schemas.RobotResponse:
    robot = usecases.get_robot(db, id=robot_id)  # type: ignore
    if robot is None:
        raise HTTPException(status_code=404, detail="Robot not found")

    return robot  # type: ignore
