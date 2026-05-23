from app.models.course_model import CourseModel
from sqlalchemy.orm import Session
from sqlalchemy import select


class CourseRepository:
    def findAll_courses(self, db: Session) -> list[CourseModel]:
        stmt = select(CourseModel)
        courses = db.scalars(stmt).all()

        return list(courses)
    
    def findById_courses(self, course_id: int, db: Session) -> CourseModel | None: 
        stmt = select(CourseModel).where(CourseModel.id == course_id)
        course = db.scalar(stmt)

        return course
    
    def create_courses(self, course: CourseModel, db: Session) -> CourseModel: 
        db.add(course)
        db.commit()
        db.refresh(course)

        return course
    
    def update_courses(self, course: CourseModel, db: Session) -> CourseModel:
        db.add(course)
        db.commit()
        db.refresh(course)

        return course

    
    def delete_courses(self, course: CourseModel, db: Session) -> CourseModel | None:
        db.delete(course)
        db.commit()

        return course 