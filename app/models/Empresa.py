from app.db.database import Base
from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import mapped_column


class Empresa(Base):
    __tablename__ = "empresa"
    id: int = mapped_column(Integer, primary_key=True, index=True)
    empresanome: str = mapped_column(String(100), nullable=False)
    empresadocumento: str = mapped_column(String(20), unique=True, nullable=False)
    empresaemail: str = mapped_column(String(100), unique=True, nullable=False)
    empresaatcreate: DateTime = mapped_column(DateTime, nullable=False)
    empresaatupdate: DateTime = mapped_column(DateTime, nullable=True)
    empresaclienteid: int = mapped_column(Integer, nullable=False)