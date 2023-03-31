from sqlmodel import Field, SQLModel
from uuid import uuid4, UUID
from datetime import datetime
from typing import Optional


class BaseModel(SQLModel):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class BaseFilter():
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class BaseUpdate():
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class BaseManyToManyRelationShip():
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
