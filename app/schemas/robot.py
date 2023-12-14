from pydantic import BaseModel


class RobotResponse(BaseModel):
    id: int
    name: str


class RobotCreate(BaseModel):
    name: str


class RobotUpdate(BaseModel):
    id: int
    name: str
