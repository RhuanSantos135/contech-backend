from fastapi import APIRouter, HTTPException, status, Depends, Request
from app.models.Usuario import Usuario
from sqlalchemy.orm import Session
from app.db.database import get_database
from app.security.auth import get_hash


router = APIRouter(prefix="/usuarios", tags=["Usuario"])


@router.get("/")
def get_usuarios(request: Request, db: Session = Depends(get_database)):
    try:
        usuario = db.query(Usuario).all()
        if not usuario:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario nao encontrado")
        return usuario
    
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"{e}")