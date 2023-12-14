from app import models

# from app.deps import DatabaseDep
from app.deps import get_db


def seed():
    db = next(get_db())

    if db.query(models.Robot.id).count() > 0:
        print("skip seed")
        return

    db.add(models.Robot(name="R2D2"))
    db.commit()
