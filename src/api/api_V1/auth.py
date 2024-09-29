from fastapi import APIRouter

from core import settings
from core.schemas.user import UserRead, UserCreate
from .fastapi_users_router import fastapi_users
from api.dependencies.auth.backend import auth_backend

router = APIRouter(
    prefix=settings.api.v1.auth,
    tags=["Auth"],
)

# /login & /logout
router.include_router(
    router=fastapi_users.get_auth_router(auth_backend),
)

# /register
router.include_router(
    router=fastapi_users.get_register_router(UserRead, UserCreate),
)
