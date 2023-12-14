from pydantic import BaseModel


class RobotResponse(BaseModel):
    id: int
    name: str
