from pydantic import BaseModel, Field

class CreateUser(BaseModel):
    name: str 
    username: str
    password: int
