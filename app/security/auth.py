from pwdlib import PasswordHash
from datetime import datetime, timedelta, timezone
from .schema import Token
from jwt import encode
from zoneinfo import ZoneInfo
from app.conf.conf import ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY, ALGORITHM


context =  PasswordHash.recommended()

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