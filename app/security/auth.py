from pwdlib import PasswordHash
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException , status
from sqlalchemy.orm import Session
from db.database import get_database
from models.Usuario import Usuario
from jwt import encode, decode, DecodeError
from zoneinfo import ZoneInfo
from app.conf.conf import ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY, ALGORITHM


context =  PasswordHash.recommended()

oauth2_scheme= OAuth2PasswordBearer(tokenUrl="/api/auth")

def get_hash(password: str):
    return context.hash(password)

def verify_hash(password: str , password_hash: str):
    return context.verify(password, password_hash)

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(tz=ZoneInfo('UTC')) + timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({'exp': expire})
    encode_jwt = encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encode_jwt

def get_current_user(db: Session = Depends(get_database), token: str =  Depends(oauth2_scheme)):
    
    credentials_exception = HTTPException(
        status_code=status.UNAUTHORIZED,
        detail='Could not validate credentials',
        headers={'WWW-Authenticate': 'Bearer'},
    )
    try:
        payload = decode(token, SECRET_KEY)
        subject_email = payload.get('sub')
        if not subject_email:
            raise credentials_exception
        user = db.query(Usuario).filter(Usuario.usuarioemail == subject_email).first()
        if not user:
            raise credentials_exception
        return user
    except DecodeError:
        raise credentials_exception
    ...