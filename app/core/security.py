from datetime import datetime, timedelta, timezone
from typing import Optional
from jose import jwt, JWTError
import bcrypt
from app.core.config import settings

"""
1 - Função Hash de Senha

- Recebe uma senha em texto
- Gere o hash utilizando bcrypt
- Retorne o hash gerado como str 
"""
def hash_password(password: str) -> str:
    password_bytes = password.encode()
    salt_bytes = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password_bytes, salt_bytes)

    return hashed_password.decode('utf-8')

"""
2 - Função Verificação de Senha

-Compara uma senha em texto puro enviado pelo cliente com o hash criptografado armanzeado no banco de dados
- Retorna ao usuário um bool True caso as senha batam, False caso contrário
"""
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode(), hashed_password.encode())

"""
3 - Função Criar JWT

- Função primária que gere um token JWT
"""
def create_token(data: dict, experies_delta: timedelta) -> str:
    payload = data.copy()
    payload["exp"] = datetime.now(timezone.utc) + experies_delta
    return jwt.encode(payload, settings.secret_key, algorithm=settings.algorithm)

"""
3 - Função JWT Acess Token

-Gera um Token de Acesso (Access Token) de curta duração.
-Este token identifica o usuário, carrega seu nível de permissão (role) 
- Token é enviado nas requisições subsequentes para autorizar o acesso às rotas protegidas da API.
"""

def create_access_token(user_id: int, role: str) -> str:
    return create_token(
        {"sub": str(user_id), "role": role, "type": "access"},
        timedelta(minutes=settings.access_token_expire_minutes),

        )

"""
4 - Função JWT Refresh Token

-Gera um Token de Atualização (Refresh Token) de longa duração.
-Não carrega permissões de rotas; serve exclusivamente para o cliente solicitara renovação de um novo Access Token válido sem exigir o login com e-mail e senha novamente.
"""

def create_refresh_token(user_id: int) -> str:
    return create_token(
        {"sub": str(user_id), "type": "refresh"},
        timedelta(days=settings.refresh_token_expire_days),

        )

"""
5 - Função JWT decode Token

- Decodifica o token JWT enviado pelo cliente utilizando a chave secreta do servidor.
- Verifica a integridade da assinatura e se o token ainda está dentro do prazo de validade.
- Retorna o dicionário com os dados do payload se o token for válido, ou None caso o token tenha sido adulterado ou já esteja expirado.
"""

def decode_token(token: str) -> Optional[dict]:
    try:
        return jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
    except JWTError:
        return None









