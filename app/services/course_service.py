from fastapi import HTTPException, status
from typing import Sequence
from app.repositories.course_repository import CourseRepository
from app.models.course_model import CourseModel
from app.schemas.course_schema import CourseCreate, CourseUpdate
from sqlalchemy.orm import Session

class CourseService:
    def __init__(self):
        self.repository = CourseRepository()
    
    def get_all_courses(self, db: Session) -> Sequence[CourseModel]:
        courses = self.repository.findAll_courses(db)

        if not courses:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Nenhum curso cadastrado")
        
        return courses
    
    def get_course_by_id(self, course_id: int, db: Session) -> CourseModel:
        course = self.repository.findById_courses(course_id, db)
        if not course:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")
        
        return course
    
    def create_course(self, course_data: CourseCreate, db: Session) -> CourseModel:
        course = CourseModel(**course_data.model_dump())

        return self.repository.create_courses(course, db)
    
    def update_course(self, course_id: int, course_data: CourseUpdate, db: Session) -> CourseModel:
        course = self.repository.findById_courses(course_id, db)
        if not course:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")
        
        update_course_data = course_data.model_dump(exclude_unset=True)
        for c, v in update_course_data.items():
            setattr(course, c, v)
        
        return self.repository.update_courses(course, db)
    
    def delete_course(self, course_id: int, db: Session) -> None:
        course = self.repository.findById_courses(course_id, db)
        if not course:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")
        
        return self.repository.delete_courses(course, db)