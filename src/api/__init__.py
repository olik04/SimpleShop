from fastapi import APIRouter
from .user.views import router as users_router

router = APIRouter()

router.include_router(router=users_router, prefix="/users")
