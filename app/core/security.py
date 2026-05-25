from datetime import datetime, timedelta, timezone
from typing import Optional
from jose import jwt, JWTError
import bcrypt

"""
1 - Função Responsável por criptografar senha
"""
def hash_password(password: str) -> str:
    password_bytes = password.encode()
    salt_bytes = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password_bytes, salt_bytes)

    return hashed_password

"""
2 - Função Responsável verificar se a senha enviada pelo usuário é a mesma que a senha hash salva no banco de dados
"""
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode(), hashed_password.encode())

"""
3 - Função responsável por gerar um token JWT
"""
def create_token(data: dict, experies_delta: timedelta) -> str:
    payload = data.copy()
    payload["exp"] = datetime.now(timezone.utc) + experies_delta
    return jwt.encode(payload)



