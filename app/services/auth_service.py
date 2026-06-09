from fastapi import HTTPException, status
from typing import Sequence
from app.repositories.auth_repository import Auth_Repository
from app.models.auth_model import RefreshToken
from app.schemas.auth_schema import LoginRequest, RequestRefreshToken 
from sqlalchemy.orm import Session

class AuthService():
    def __init__(self):
        pass