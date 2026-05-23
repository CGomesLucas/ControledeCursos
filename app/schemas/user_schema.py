from pydantic import BaseModel, Field, EmailStr

class CreateUser(BaseModel):
    name: str 
    email: EmailStr
    password: int

class ResponseUser(BaseModel):
    id: int
    name: str
    email: EmailStr
    active: bool
