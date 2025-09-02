from pydantic import BaseModel
from datetime import datetime

class EmpresaCreate(BaseModel):
    empresanome: str
    empresaemail: str
    empresadocumento: str
    empresaclienteid: int