from typing import List, TYPE_CHECKING
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from app.core.database import Base
from app.models.learning_path_has_course import learning_path_has_course

if TYPE_CHECKING:
    from app.models.course_model import CourseModel

class LearningPathModel(Base):
    __tablename__ = "learning-path"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(150), nullable=True)
    link_image: Mapped[str] = mapped_column(String(255), nullable=False)
    link_video: Mapped[str] = mapped_column(String(255), nullable=False)
    material_content: Mapped[str] = mapped_column(String(255), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    courses: Mapped[List["CourseModel"]] = relationship(
        secondary=learning_path_has_course,
        back_populates="learning_paths"
    )


