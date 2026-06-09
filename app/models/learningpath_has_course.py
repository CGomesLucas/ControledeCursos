from sqlalchemy import Integer, String, Boolean, DateTime, Table, Column, ForeignKey
from app.core.database import Base

learning_path_has_course = Table(
    "learning_path_has_course",
    Base.metadata,
    Column("id_courses", Integer, ForeignKey("courses.id"), primary_key=True),
    Column("id_learningpath", Integer, ForeignKey("learning-path.id"), primary_key=True) 
)

