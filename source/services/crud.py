from typing import Optional
from uuid import UUID
from sqlmodel import SQLModel, select

from config.database import Connection
from sqlmodel.sql.expression import SelectOfScalar


class CRUDService:
    model = SQLModel
    update_model = SQLModel
    filter_model = SQLModel

    def all(self, limit: int = 0, offset: int = 0, filter: Optional[filter_model] = None) -> list[model]:
        with Connection.get_session() as session:
            query = self.__get_query_set()
            query = self.__limit(query, limit)
            query = self.__offset(query, offset)
            query = self.__add_filters(query, filter)

            data = session.exec(query).all()

            return data

    def __get_query_set(self):
        return select(self.model)

    def __limit(self, query: SelectOfScalar, limit: int):
        if limit:
            query = query.limit(limit)
        return query

    def __offset(self, query: SelectOfScalar, offset: int):
        if offset:
            query = query.offset(offset)
        return query

    def __add_filters(self, query: SelectOfScalar, filter: Optional[filter_model]):
        if filter:
            # TODO: Filter Adding System
            pass
        return query

    def get(self, id: UUID):
        with Connection.get_session() as session:
            return session.get(self.model, id)

    def delete(self, id: UUID) -> dict:
        with Connection.get_session() as session:
            instance = session.get(self.model, id)
            session.delete(instance)
            session.commit()
            return {
                "id": id,
                "deleted": True
            }

    def create(self):
        with Connection.get_session() as session:
            return "GET"

    def update(self):
        with Connection.get_session() as session:
            return "GET"
