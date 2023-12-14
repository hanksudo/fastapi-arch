from infra.database import get_db

from app import models


def seed():
    with get_db() as db:
        if db.query(models.Robot).count() > 0:
            print("skip seed")
            return

        db.add(models.Robot(name="R2D2"))
        db.commit()
