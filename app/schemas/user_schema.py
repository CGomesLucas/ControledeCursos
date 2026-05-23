from pydantic import BaseModel, Field, EmailStr

class CreateUser(BaseModel):
    name: str 
    email: EmailStr
    password: str

class UpdateUser(BaseModel):
    name: str | None = None
    email: EmailStr | None = None
    password: str | None = None

class ResponseUser(BaseModel):
    id: int
    name: str
    email: EmailStr
    active: bool

    class Config:
        from_attributes = True
