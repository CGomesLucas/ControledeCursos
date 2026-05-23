from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.user_schema import CreateUser, ResponseUser, UpdateUser
from app.models.user_model import UserModel
from app.core.database import get_db

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/", response_model=list[ResponseUser])
def findAll_users(db: Session = Depends(get_db)):
    users = db.query(UserModel).all()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuários não encontrados")

    return users

@router.get("/{user_id}", response_model=ResponseUser)
def findById_users(user_id: int, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuário não encontrado")

    return user

@router.put("/{user_id}", response_model=ResponseUser)
def update_users(user_id: int, user: UpdateUser, db: Session = Depends(get_db)):
    new_user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not new_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuário não encontrado")

    for key, value in user.model_dump(exclude_unset=True).items():
        setattr(new_user, key, value)

    db.commit()
    db.refresh(new_user)

    return new_user

@router.post("/", response_model=ResponseUser, status_code=status.HTTP_201_CREATED)
def create_users(user: CreateUser, db: Session = Depends(get_db)):
    new_user = UserModel(**user.model_dump())

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.delete("/{user_id}")
def delete_users(user_id: int,db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuário não encontrado")
    
    db.delete(user)
    db.commit()

    return {"message": "Usuário deletado com sucesso"}
    

