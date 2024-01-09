import json
from fastapi import APIRouter, Depends, Response, HTTPException
from app.internal import schemas
from app.internal.usecases import RobotUseCase
from app.internal.deps import provider

router = APIRouter()

@router.get("/{robot_id}", response_model=schemas.RobotResponse)
async def get_robot( 
    robot_id: int,
    usecase: RobotUseCase = Depends(provider.NewRobotUseCase)
) -> schemas.RobotResponse | Response:
    robot = usecase.get_robot(robot_id)
    if robot is None:
        return Response(status_code=404, content=json.dumps({"message": "robot not found"}))

    return robot  # type: ignore

@router.get("", response_model=list[schemas.RobotResponse])
async def list_robots(usecase: RobotUseCase = Depends(provider.NewRobotUseCase)) -> list[schemas.RobotResponse]:
    return usecase.list_robots()  # type: ignore


@router.post("", response_model=schemas.RobotResponse)
async def create_robot(
    robot: schemas.RobotCreate,
    usecase: RobotUseCase = Depends(provider.NewRobotUseCase),
) -> schemas.RobotResponse:
    return usecase.create_robot(createSchema=robot)  # type: ignore


@router.put("/{robot_id}", response_model=schemas.RobotResponse)
async def update_robot(
    robot_id: int, 
    robot: schemas.RobotUpdate,
    usecase: RobotUseCase = Depends(provider.NewRobotUseCase),
) -> schemas.RobotResponse | Response:
    try:
        return usecase.update_robot(id=robot_id, updateSchema=robot)  # type: ignore
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{robot_id}")
async def delete_robot(
    robot_id: int, 
    usecase: RobotUseCase = Depends(provider.NewRobotUseCase),
) -> None:
    try:
        usecase.delete_robot(id=robot_id)  # type: ignore
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
