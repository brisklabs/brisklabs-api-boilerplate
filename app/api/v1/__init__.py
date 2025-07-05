from fastapi import APIRouter
from .endpoints import auth, user

router = APIRouter()
router.include_router(auth.router, prefix="/auth")
router.include_router(user.router, prefix="/user")