from pydantic import BaseModel

class ClienteCreate(BaseModel):
    clientenome: str
    clienteemail: str
    clientedocumento: str

class ClienteResponse(BaseModel):
    clientenome: str
    clienteemail: str
    clienteatcreate: str
