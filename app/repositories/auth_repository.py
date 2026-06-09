from app.models.auth_model import RefreshToken
from app.schemas.auth_schema import LoginRequest, RequestRefreshToken, ResponseRefreshToken, LoginResponseTokens
from sqlalchemy.orm import Session
from sqlalchemy import select

class Auth_Repository:
    def auth_login(self, body: RefreshToken, db: Session) -> LoginResponseTokens:
        db.add(body)
        db.commit()
        db.refresh()

        return body
    
    def auth_refresh(self, body: RefreshToken, db: Session) -> ResponseRefreshToken:
        db.add(body)
        db.commit()
        db.refresh

    