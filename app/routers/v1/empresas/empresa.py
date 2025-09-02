from fastapi import APIRouter, Depends, HTTPException, status, Request
from sqlalchemy.orm import Session
from app.db.database import get_database
from app.models.Empresa import Empresa
from .schemas import EmpresaCreate
from datetime import datetime
from app.models.Usuario import Usuario
from app.security.auth import get_current_user
from app.utils.validations import only_digits
router = APIRouter(prefix="/empresas", tags=["Empresa"])



@router.get("/" , status_code=status.HTTP_200_OK)
def get_empresa(request: Request, db: Session = Depends(get_database), current_user: Usuario = Depends(get_current_user)):
    
    try:
        empresa = db.query(Empresa).filter(Empresa.id ==  current_user.usuarioempresaid).all()
        if not empresa:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Nenhuma empresa cadastrada")  
        return empresa
    except Exception:
        raise
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"{e}")
    

@router.post("/create", status_code=status.HTTP_201_CREATED)
def create_empresa(request: Request, empresa: EmpresaCreate, db: Session = Depends(get_database)):
    
    try:
        empresa_exist = db.query(Empresa).filter(Empresa.empresadocumento == only_digits(empresa.empresadocumento)).first()
        if empresa_exist:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Empresa ja existe")        
        new_empresa = Empresa(
            empresanome=empresa.empresanome,
            empresaemail=empresa.empresaemail,
            empresadocumento=empresa.empresadocumento,
            empresaatcreate=datetime.now(),
            empresaatupdate=datetime.now(),
            empresaclienteid=empresa.empresaclienteid
        )
        db.add(new_empresa)
        db.flush()
        return {"message": "Empresa criada com sucesso", 
                "empresa": {
                    "Nome Empresa": new_empresa.empresanome,
                    "Documento Empresa": new_empresa.empresadocumento
                }}
    except Exception:
        raise
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"{e}")
            

@router.delete("/delete/{idempresa}", status_code=status.HTTP_200_OK)
def delete_empresa(request: Request, idempresa: int, db: Session = Depends(get_database), current_user: Usuario = Depends(get_current_user)):

    try:
        empresa = db.query(Empresa).filter(Empresa.id == idempresa).first()
        if not empresa:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Empresa não existe ou já excluida!")
        db.delete(empresa)
        db.flush()
    except Exception:
        raise
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"{e}")
    ...
