from fastapi import APIRouter, Depends, status
from app.schemas.course_schema import CourseCreate, CourseResponse, CourseUpdate
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.course_service import CourseService

router = APIRouter(prefix="/courses", tags=["Courses"])

@router.get("/", response_model=list[CourseResponse])
def findAll_Courses(db: Session = Depends(get_db)):
    service = CourseService()
    return service.get_all_courses(db)

@router.get("/{course_id}", response_model=CourseResponse)
def findById_Courses(course_id: int, db: Session = Depends(get_db)):
    service = CourseService()
    return service.get_course_by_id(course_id, db)
    
@router.post("/", response_model=CourseResponse, status_code=status.HTTP_201_CREATED)
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    service = CourseService()
    return service.create_course(course, db)

@router.put("/{course_id}", response_model=CourseResponse)
def update_course(course_id: int, course: CourseUpdate, db: Session = Depends(get_db)):
    service = CourseService()
    return service.update_course(course_id, course, db) 

@router.delete("/{course_id}")
def delete_course(course_id: int, db: Session = Depends(get_db)):
    service = CourseService()
    service.delete_course(course_id, db)

    return {"detail": "Curso deletado com sucesso"}




