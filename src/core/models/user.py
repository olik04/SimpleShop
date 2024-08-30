from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase

from . import Base


class User(Base, SQLAlchemyBaseUserTable[int]):
    pass
