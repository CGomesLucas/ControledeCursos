from fastapi import APIRouter
from pydantic import BaseModel, Field

router = APIRouter(prefix="/user", tags=["Users"])

class User(BaseModel):
    username: str
    password: int

@router.get("/")
def read_users():
    return {"message": "Retornando Usuários"}

@router.post("/")
def create_users(user: User):
    return {"Users": user}

@router.put("/{user_id}")
def update_users(user: User):
    return {"Users": user}

@router.delete("/{user_id}")
def delete_users(user: User):
    return {"Users": user}

