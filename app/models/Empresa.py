from app.db.database import Base
from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import mapped_column, Mapped


class Empresa(Base):
    __tablename__ = "empresa"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    empresanome: Mapped[str] = mapped_column(String(100), nullable=False)
    empresadocumento: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    empresaemail: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    empresaatcreate: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    empresaatupdate: Mapped[DateTime] = mapped_column(DateTime, nullable=True)
    empresaclienteid: Mapped[int] = mapped_column(Integer, nullable=False)