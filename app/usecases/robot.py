from app import schemas


def get_robot(id: int) -> schemas.RobotResponse:
    return schemas.RobotResponse(
        id=id,
        name="Robot",
    )
