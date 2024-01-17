from pydantic import BaseModel, ConfigDict


class RobotResponse(BaseModel):
    id: int
    name: str

    model_config = ConfigDict(from_attributes=True)  # type: ignore


class RobotCreate(BaseModel):
    name: str


class RobotUpdate(RobotCreate):
    ...
