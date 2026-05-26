from pydantic import BaseModel, Field, EmailStr 
from datetime import datetime
from typing import Optional

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class LoginResponseTokens(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"

class LoginResponseUserInfo(BaseModel):
    id: int
    email: EmailStr
    active: bool
    created_at: datetime
    role: str

class RequestRefreshToken(BaseModel):
    refresh_token: str
    token_type: str = "bearer"

class ResponseRefreshToken(BaseModel):
    access_token: str
    token_type: str = "bearer"





    

