from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto


class User(db.Model, IDto):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)
    surname = db.Column(db.String(45), nullable=True)

    def put_into_dto(self) -> Dict[str, Any]:
        return {"id": self.id, "name": self.name, "surname": self.surname}

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]):
        return User(**dto_dict)

