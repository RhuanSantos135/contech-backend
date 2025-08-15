from fastapi import APIRouter
from .Usuario.usuario import router as usuario_router


router = APIRouter(prefix="/api")

router.include_router(usuario_router)
