from fastapi import HTTPException, status
from pydantic import EmailStr
from typing import Sequence
from app.models.user_model import UserModel
from sqlalchemy.orm import Session
from app.schemas.user_schema import CreateUser, UpdateUser
from app.repositories.user_repository import UserRepository


class UserService:
    def __init__(self):
        self.repository = UserRepository()
    
    def get_all_users(self, db: Session) -> Sequence[UserModel]:
        users = self.repository.findAll_users(db)

        if not users:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Nenhum usuário cadastrado")
        
        return users
    
    def get_users_by_id(self, user_id: int, db: Session) -> UserModel:
        user = self.repository.findById_users(user_id, db)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuário não encontrado")
        
        return user
    
    def get_users_by_email(self, user_email: EmailStr, db: Session) -> UserModel:
        user = self.repository.findbyEmail_users(user_email, db)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="E-mail não encontrado")
        
        return user
    
    def create_user(self, user_data: CreateUser, db: Session) -> UserModel:
        user = UserModel(**user_data.model_dump())
        
        return self.repository.create_users(user, db)
    
    def update_user(self, user_id: int, user_data: UpdateUser, db: Session) -> UserModel:
        user = self.repository.findById_users(user_id, db)

        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuário não encontrado")
        
        user_update_data = user_data.model_dump(exclude_unset=True)
        
        for c, v in user_update_data.items():
            setattr(user, c, v)
        
        return self.repository.update_users(user, db)
    
    def delete_user(self, user_id: int, db: Session) -> None:
        user = self.repository.findById_users(user_id, db)

        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuário não encontrado")
        
        self.repository.delete_users(user, db)