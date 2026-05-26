from sqlalchemy.orm import Session
from sqlalchemy import select
from pydantic import EmailStr
from app.models.user_model import UserModel

class UserRepository:
    
    def findAll_users(self, db: Session) -> list[UserModel]:
        stmt = select(UserModel)
        users = db.scalars(stmt).all()

        return list(users)
    
    def findById_users(self, user_id: int, db: Session) -> UserModel | None: 
        stmt = select(UserModel).where(UserModel.id == user_id)
        user = db.scalar(stmt)

        return user
    
    def findbyEmail_users(self, user_email: EmailStr, db: Session) -> UserModel | None:
        stmt = select(UserModel).where(UserModel.email == user_email)
        user = db.scalar(stmt)

        return user
    
    def create_users(self, user: UserModel, db: Session) -> UserModel: 
        db.add(user)
        db.commit()
        db.refresh(user)

        return user
    
    def update_users(self, user: UserModel, db: Session) -> UserModel:
        db.add(user)
        db.commit()
        db.refresh(user)

        return user

    
    def delete_users(self, user: UserModel, db: Session) -> None:
        db.delete(user)
        db.commit()

    
        
    
    
    




