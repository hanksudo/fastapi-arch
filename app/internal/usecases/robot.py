from app.internal.models import Robot
from app.internal.repositories import RobotRepository

class RobotUseCase:
    def __init__(self, robot_repo: RobotRepository):
        self.robot_repo: RobotRepository = robot_repo

    def get_robot(self, id: int) -> Robot | None:
        return self.robot_repo.get(id)