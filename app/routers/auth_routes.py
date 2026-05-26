from fastapi import APIRouter, Depends, HTTPException 
from sqlalchemy.orm import Session
from app.core.database import get_db
from schemas.auth_schema import LoginResponseUserInfo, LoginResponseTokens, LoginRequest, ResponseRefreshToken, RequestRefreshToken

app = APIRouter(prefix="/auths", tags="Auths")

@app.post("/login")
def login(body: LoginRequest, db: Session = Depends(get_db)):
    







