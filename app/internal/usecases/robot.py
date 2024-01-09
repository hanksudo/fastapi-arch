from app.internal.models import Robot
from app.internal.schemas import RobotCreate, RobotUpdate
from app.internal.repositories import RobotRepository

class RobotUseCase:
    def __init__(self, robot_repo: RobotRepository):
        self.robot_repo: RobotRepository = robot_repo

    def get_robot(self, id: int) -> Robot | None:
        """Get robot by id"""
        return self.robot_repo.get(id)

    def list_robots(self) -> list[Robot]:
        """List all robots"""
        return self.robot_repo.list_all()
    
    def create_robot(self, *, createSchema: RobotCreate) -> Robot:
        """Create robot"""
        return self.robot_repo.create(obj_in=createSchema)

    def update_robot(self, *, id: int, updateSchema: RobotUpdate) -> Robot:
        """Update robot"""
        robot = self.robot_repo.get(id)
        if robot is None:
            raise Exception("robot not found")
        return self.robot_repo.update(db_obj=robot, obj_in=updateSchema)
    
    def delete_robot(self, *, id: int) -> None:
        """Delete robot"""
        robot = self.robot_repo.get(id)
        if robot is None:
            raise Exception("robot not found")
        self.robot_repo.delete(id=robot.id)