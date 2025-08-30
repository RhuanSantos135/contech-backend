from app.db.database import Base
from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import mapped_column    


class Cupon(Base):
    __tablename__ = "cupon"
    id: int = mapped_column(Integer, primary_key=True, index=True)
    cuponcode: str = mapped_column(String(50), nullable=False)
    cuponprodutoid: int = mapped_column(Integer, nullable=False)
    cuponquantidade: int = mapped_column(Integer, nullable=False)
    cuponprodutopreco: float = mapped_column(nullable=False)
    cupondesconto: float = mapped_column(nullable=False)
    cuponatcreate: DateTime = mapped_column(DateTime, nullable=False)
    cuponatupdate: DateTime = mapped_column(DateTime, nullable=True)
    cuponempresaid: int = mapped_column(Integer, nullable=False)