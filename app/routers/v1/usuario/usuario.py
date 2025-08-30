from fastapi import APIRouter, HTTPException, status, Depends, Request
from app.models.Usuario import Usuario
from sqlalchemy.orm import Session
from app.db.database import get_database
from app.security.auth import get_hash
from .schemas import UsuarioCreate


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
    

@router.post("/create", status_code=status.HTTP_201_CREATED)
def create_usuario(request: Request, usuario: UsuarioCreate, db: Session = Depends(get_database)):
    try:
        usuario_exist = db.query(Usuario).filter(Usuario.usuarioemail == usuario.usuarioemail).first()
        if usuario_exist:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Usuario ja existe")
        

        new_usuario = Usuario(
            usuarionome=usuario.usuarionome,
            usuariosenha=get_hash(usuario.usuariosenha),
            usuarioemail=usuario.usuarioemail,
            usuarioempresaid=usuario.usuarioempresaid
        )
        db.add(new_usuario)
        db.commit()
        db.refresh(new_usuario)
        return {"message": "Usuario criado com sucesso", "usuario": new_usuario}
    
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"{e}")
    

@router.delete("/delete/{idusuario}", status_code=status.HTTP_200_OK)
def delete_usuario(idusuario: int, db: Session = Depends(get_database)):
    try:
        usuario_not_found = db.query(Usuario).filter(Usuario.id == idusuario).first()
        if not usuario_not_found:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario nao encontrado")
        
        db.delete(usuario_not_found)
        db.commit()
        return {"message": "Usuario deletado com sucesso"}
    
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"{e}")
    ...
