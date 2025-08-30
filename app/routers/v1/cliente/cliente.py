from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status, Request
from app.db.database import get_database
from app.models.Cliente import Cliente
from .schemas import ClienteCreate  , ClienteResponse
from datetime import datetime


router = APIRouter(prefix="/clientes", tags=["Cliente"])


@router.post("/create", status_code=status.HTTP_201_CREATED, response_model=ClienteResponse)
def create_cliente(request: Request, cliente: ClienteCreate, db: Session = Depends(get_database)):
    try:
        cliente_exist = db.query(Cliente).filter(Cliente.clienteemail == cliente.clienteemail).first()
        if cliente_exist:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Cliente ja existe")       
        
        new_cliente = Cliente(
            clientenome=cliente.clientenome,
            clienteemail=cliente.clienteemail,
            clientedocumento=cliente.clientedocumento,
            clienteatcreate=datetime.now(),
            clienteatupdate=datetime.now()
        )
        db.add(new_cliente)
        db.refresh(new_cliente)
        
        return {"message": "Cliente criado com sucesso", "cliente": new_cliente}
    
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"{e}")
    

