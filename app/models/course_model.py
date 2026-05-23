from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey, JSON
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.database import Base

class CourseModel(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True) 
    course_hours = Column(Integer, nullable=False)
    activated = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime) 
    related_topics = Column(JSON, default=list)
    authors = relationship("AuthorModel", back_populates="course", cascade="all, delete-orphan")


class AuthorModel(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    course_id = Column(Integer, ForeignKey("courses.id", ondelete="CASCADE"))
    course = relationship("CourseModel", back_populates="authors")