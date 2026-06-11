from typing import TYPE_CHECKING
from sqlalchemy import Integer, String, Boolean, DateTime, Date, Enum as SQLEnum, Numeric
from decimal import Decimal
from enum import Enum
from app.core.database import Base
from datetime import datetime, date
from sqlalchemy.orm import Mapped, mapped_column

if TYPE_CHECKING:
    from app.models.module_model import ModuleModel

class TypeApplication(Enum):
    CURSO = "Curso"
    TRILHA = "Trilha"
    FORMACAO = "Formacão"


class ModuleModel(Base):
    __tablename__ = "modules"

    id_module: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    id_reference: Mapped[int] = mapped_column(Integer, nullable=False)
    type_application: Mapped[TypeApplication] = mapped_column(SQLEnum(TypeApplication), nullable=False)
    module_application_data: Mapped[date] = mapped_column(Date, default=date.today()) 
    module_application_ending: Mapped[date] = mapped_column(Date, nullable=False)
    module_duration: Mapped[str] = mapped_column(String(30), nullable=False)
    total_spots: Mapped[int] = mapped_column(Integer, nullable=False)
    price: Mapped[Decimal] = mapped_column(Numeric(precision=6, scale=2), nullable=False)
    warning_message: Mapped[str] = mapped_column(String(255), nullable=False)
    is_offer: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)






