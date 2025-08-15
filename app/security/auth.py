from pwdlib import PasswordHash

context =  PasswordHash.recommended()

def get_hash(password: str):
    return context.hash(password)

def verify_hash(password: str , password_hash: str):
    return context.verify(password, password_hash)