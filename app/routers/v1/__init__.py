from fastapi import APIRouter
from .usuario.usuario import router as usuario_router
from .auth.auth import router as auth_router
from .cliente.cliente import router as cliente_router
from .empresas.empresa import router as empresa_router

router = APIRouter(prefix="/api/v1")

list_routers = [usuario_router, cliente_router, auth_router, empresa_router]

for r in list_routers:
    router.include_router(r)