from core.database import Base
from sqlalchemy import Column, String, Integer, Float, Boolean, DateTime, ForeignKey

class UserModel(Base):
    __tablename__ = "users"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String, nullable=False)
    email = Column("email", String, unique=True, nullable=False)
    password = Column("senha", String, nullable=False)
    active = Column("active", Boolean, default=True)

