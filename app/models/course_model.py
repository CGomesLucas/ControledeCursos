from typing import List, TYPE_CHECKING
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey, JSON
from sqlalchemy.orm import relationship, Mapped
from datetime import datetime
from app.core.database import Base
from app.models.learning_path_has_course import learning_path_has_course

if TYPE_CHECKING:
    from app.models.learning_path import LearningPathModel

class CourseModel(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    price = Column(String, nullable=False)
    description = Column(String, nullable=True) 
    course_hours = Column(Integer, nullable=False)
    activated = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.now) 
    related_topics = Column(JSON, default=list)

    learning_paths: Mapped[List["LearningPathModel"]] = relationship(
        secondary=learning_path_has_course,
        back_populates="courses"
    )
