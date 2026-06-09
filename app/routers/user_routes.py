from fastapi import APIRouter, Depends, status
from pydantic import EmailStr
from sqlalchemy.orm import Session
from app.schemas.user_schema import CreateUser, ResponseUser, UpdateUser
from app.services.user_service import UserService
from app.core.database import get_db

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/", response_model=list[ResponseUser])
def findAll_users(db: Session = Depends(get_db)):
    service = UserService()
    return service.get_all_users(db)

@router.get("/{user_id}", response_model=ResponseUser)
def findById_users(user_id: int, db: Session = Depends(get_db)):
    service = UserService()
    return service.get_users_by_id(user_id, db)

@router.get("/{email}", response_model=ResponseUser)
def findByEmail_users(user_email: EmailStr, db: Session = Depends(get_db)):
    service = UserService()
    return service.get_users_by_email(user_email, db)

@router.put("/{user_id}", response_model=ResponseUser)
def update_users(user_id: int, user: UpdateUser, db: Session = Depends(get_db)):
    service = UserService()
    return service.update_user(user_id, user, db)

@router.post("/", response_model=ResponseUser, status_code=status.HTTP_201_CREATED)
def create_users(user: CreateUser, db: Session = Depends(get_db)):
    service = UserService()
    return service.create_user(user, db)

@router.delete("/{user_id}")
def delete_users(user_id: int,db: Session = Depends(get_db)):
    service = UserService()
    service.delete_user(user_id, db)

    return {"detail": "Usuário deletado com sucesso"}

