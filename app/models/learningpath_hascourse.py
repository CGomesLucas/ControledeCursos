from sqlalchemy import Table, Column, Integer, ForeignKey
from app.core.database import Base

learning_path_has_course = Table(
    "learning_path_has_course",
    Base.metadata,
    Column("id_courses", Integer, ForeignKey("courses.id", ondelete="CASCADE"), primary_key=True),
    Column("id_learningpath", Integer, ForeignKey("learning_path.id", ondelete="CASCADE"), primary_key=True)
)