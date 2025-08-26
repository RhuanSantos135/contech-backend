from fastapi import APIRouter
from .usuario.usuario import router as usuario_router
from .auth.auth import router as auth_router

router = APIRouter(prefix="/api")

router.include_router(usuario_router)
router.include_router(auth_router)
