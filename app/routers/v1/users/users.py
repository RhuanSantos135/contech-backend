from fastapi import APIRouter
from app.db.database import supabase

router = APIRouter()


@router.get("/users")
def get_users():
    response = (
        supabase.table("usuario").select("*").execute()
    )
    return response