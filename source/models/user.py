from typing import Optional
from models.base import BaseModel, BaseUpdate, BaseFilter


class User(BaseModel, table=True):
    name: str


class UserUpdate(BaseUpdate):
    name: Optional[str] = None


class UserFilter(BaseFilter):
    name: Optional[str] = None
