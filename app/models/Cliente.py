from app.db.database import Base
from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import mapped_column, Mapped

class Cliente(Base):
    __tablename__ = "cliente"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    clientenome: Mapped[str] = mapped_column(String(100), nullable=False)
    clientedocumento: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    clienteemail: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    clienteatcreate: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    clienteatupdate: Mapped[DateTime] = mapped_column(DateTime, nullable=True)