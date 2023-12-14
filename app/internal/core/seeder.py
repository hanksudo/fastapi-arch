from internal import models
from sqlalchemy.orm import Session


class Seeder:
    db: Session

    def __init__(self, db: Session) -> None:
        self.db = db

    def is_seeded(self) -> bool:
        return self.db.query(models.Robot).count() > 0

    def seed(self) -> None:
        if self.is_seeded():
            print("skip seed")
            return

        self.db.add(models.Robot(name="R2D2"))
        self.db.commit()
