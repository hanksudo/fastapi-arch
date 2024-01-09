from contextlib import AbstractContextManager

from typing import Any, Generic, TypeVar, Callable

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session

ModelType = TypeVar("ModelType", bound=Any)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class BaseRepository(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: type[ModelType], session_factory: Callable[..., AbstractContextManager[Session]]):
        """
        **Parameters**

        * `model`: A SQLAlchemy model class
        * `schema`: A Pydantic model (schema) class
        * `session_factory`: A function that returns a context manager yielding a SQLAlchemy session
        """
        self.model = model
        self.session_factory = session_factory

    def get(self, id: Any) -> ModelType | None:
        with self.session_factory() as session:
            return session.query(self.model).get(id)
    
    def list_all(self) -> list[ModelType]:
        with self.session_factory() as session:
            return session.query(self.model).all()

    def create(self, *, obj_in: CreateSchemaType) -> ModelType:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)

        with self.session_factory() as session:
            session.add(db_obj)
            session.commit()
            session.refresh(db_obj)
        return db_obj

    def update(
        self,
    
        *,
        db_obj: ModelType,
        obj_in: UpdateSchemaType | dict[str, Any],
    ) -> ModelType:
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.model_dump(exclude_unset=True)

        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
            
            with self.session_factory() as session:
                session.add(db_obj)
                session.commit()
                session.refresh(db_obj)
        return db_obj

    def delete(self, *, id: int) -> None:
        with self.session_factory() as session:
            obj = session.query(self.model).get(id)
            session.delete(obj)
            session.commit()
