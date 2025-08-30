from app.db.database import Base
from sqlalchemy import Column, String, Integer

class Usuario(Base):
    __tablename__ = "usuario"
    id = Column(Integer, primary_key=True, autoincrement=True)
    usuarionome = Column(String)
    usuariosenha = Column(String)
    usuarioemail = Column(String)
    usuarioempresaid = Column(Integer)