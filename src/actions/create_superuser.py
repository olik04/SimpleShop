import asyncio
import contextlib

from pydantic import EmailStr

from api.dependencies.auth.users import get_users_db
from api.dependencies.auth.user_manager import get_user_manager
from core import settings
from core.auth.user_manager import UserManager
from core.models import db_helper, User
from core.schemas.user import UserCreate

# from fastapi_users.exceptions import UserAlreadyExists


get_users_db_context = contextlib.asynccontextmanager(get_users_db)
get_user_manager_context = contextlib.asynccontextmanager(get_user_manager)


async def create_user(
    user_manager: UserManager,
    user_create: UserCreate,
) -> User:
    user = await user_manager.create(
        user_create=user_create,
        safe=False,
    )
    return user


async def create_superuser(
    username: str = settings.user_defaults.username,
    email: EmailStr = settings.user_defaults.email,
    password: str = settings.user_defaults.password,
    is_active: bool = settings.user_defaults.is_active,
    is_superuser: bool = settings.user_defaults.is_superuser,
    is_verified: bool = settings.user_defaults.is_verified,
):
    user_create = UserCreate(
        username=username,
        email=email,
        password=password,
        is_active=is_active,
        is_superuser=is_superuser,
        is_verified=is_verified,
    )

    async with db_helper.session_factory() as session:
        async with get_users_db_context(session) as users_db:
            async with get_user_manager_context(users_db) as user_manager:
                return await create_user(
                    user_manager=user_manager,
                    user_create=user_create,
                )


if __name__ == "__main__":
    asyncio.run(create_superuser())
