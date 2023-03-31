import os
from dotenv import load_dotenv

from sqlmodel import SQLModel, create_engine, Session

load_dotenv()

database = "postgresql"

USERNAME = os.getenv("DB_USERNAME", "")
PASSWORD = os.getenv("DB_PASSWORD", "")
DBNAME = os.getenv("DB_NAME", "")
HOST = os.getenv("DB_HOST", "")
PORT = os.getenv("DB_PORT", "")


class Connection:
    @classmethod
    def get_engine(cls):
        url = f"{database}://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}"
        return create_engine(
            url=url,
        )

    @classmethod
    def get_session(cls):
        return Session(bind=cls.get_engine())

    @classmethod
    def create_database(cls):
        import models
        SQLModel.metadata.create_all(bind=cls.get_engine())

