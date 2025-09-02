from fastapi import APIRouter , Depends , HTTPException, status , Request
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from app.security.auth import (verify_hash , create_access_token)
from app.models.Usuario import Usuario
from app.db.database import get_database
router = APIRouter(prefix="/auth", tags=['Auth'])


@router.post("/login")
def login(request: Request , form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_database)):
    try:
        user = db.query(Usuario).filter(Usuario.usuarioemail == form_data.username).first()
       
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="user not found")
        
        if not verify_hash(form_data.password, user.usuariosenha):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="password incorrect")                
        token = create_access_token(data={"username": user.usuarioemail})
        return {
            "message": "user authenticator",
            "user": {
                "name": user.usuarionome,
                "email": user.usuarioemail,
                "host": request.client.host
            },
            "token": token
        }
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"{e}")

    ...