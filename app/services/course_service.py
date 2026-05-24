from fastapi import HTTPException, status
from app.repositories.course_repository import CourseRepository
from app.models.course_model import CourseModel
from app.schemas.course_schema import CourseCreate, CourseUpdate
from sqlalchemy.orm import Session

class CourseService:
    def __init__(self):
        self.repository = CourseRepository()
    
    def get_all_courses(self, db: Session) -> list[CourseModel]:
        return self.repository.findAll_courses(db)
    
    def get_course_by_id(self, course_id: int, db: Session) -> CourseModel:
        course = self.repository.find_by_id(course_id, db)
        if not course:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")
        
        return course
    
    def create_course(self, course_id: int, course_data: CourseCreate, db: Session) -> CourseModel:
        existing_course = self.repository.findById_courses(course_id, db)
        if existing_course:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Curso já cadastrado")
        
        course_model = CourseModel(**course_data.model.dump())
        return self.repository.create_courses(course_model, db)
    
    def update_course(self, course_id: int, course_data: CourseUpdate, db: Session) -> CourseModel:
        course = self.repository.findById_courses(course_id, db)
        if not course:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")
        
        update_course_data = course_data.model_dump(exclude_unset=True)
        for c, v in self.update_course.items():
            setattr(course, c, v)
        
        return self.repository.update_courses(course, db)
    
    def delete_course(self, course_id: int, db: Session) -> CourseModel:
        course = self.repository.findById_courses(course_id, db)
        if not course:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")
        
        return self.repository.delete_courses(course, db)