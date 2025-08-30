from pydantic import BaseModel  

class UsuarioCreate(BaseModel):
    usuarionome: str
    usuariosenha: str
    usuarioemail: str
    usuarioempresaid: int