from typing import TYPE_CHECKING

from annotated_types import MinLen, MaxLen
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

from core.models import Base

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class User(Base, SQLAlchemyBaseUserTable[int]):
    username: Mapped[str] = mapped_column(
        String(length=20), unique=True, index=True, nullable=False
    )
    #
    # @classmethod
    # def get_db(cls, session: "AsyncSession"):
    #     return SQLAlchemyUserDatabase(session, User)
