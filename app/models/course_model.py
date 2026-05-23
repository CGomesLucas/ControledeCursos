from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey, JSON
from datetime import datetime
from app.core.database import Base

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
