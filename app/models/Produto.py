from app.db.database import Base
from sqlalchemy import DateTime, Integer, String, Float
from sqlalchemy.orm import mapped_column

class Produto(Base):
    __tablename__ = "produto"
    id: int = mapped_column(Integer, primary_key=True, index=True)
    produtonome: str = mapped_column(String(100), nullable=False)
    produtopreco: float = mapped_column(nullable=False)
    produtoatcreate: DateTime = mapped_column(DateTime, nullable=False)
    produtoatupdate: DateTime = mapped_column(DateTime, nullable=True)
    produtoquantidade: float = mapped_column(Float, nullable=False)
    produtoempresaid: int = mapped_column(Integer, nullable=False)