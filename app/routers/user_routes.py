from fastapi import APIRouter
from app.schemas.user_schema import CreateUser

router = APIRouter(prefix="/user", tags=["Users"])

@router.get("/")
def read_users():
    return {"message": "Retornando Usuários"}

@router.post("/")
def create_users(user: CreateUser):
    return {"Users": user}

@router.put("/{user_id}")
def update_users(user: CreateUser):
    return {"Users": user}

@router.delete("/{user_id}")
def delete_users(user: CreateUser):
    return {"Users": user}

