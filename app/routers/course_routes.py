from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.course_schema import CourseCreate, CourseResponse, CourseUpdate
from sqlalchemy.orm import Session
from app.models.course_model import CourseModel
from app.core.database import get_db

router = APIRouter(prefix="/courses", tags=["Courses"])

@router.get("/", response_model=list[CourseResponse])
def findAll_Courses(db: Session = Depends(get_db)):
    cursos = db.query(CourseModel).all()
    return cursos

@router.get("/{course_id}", response_model=CourseResponse)
def findById_Courses(course_id: int, db: Session = Depends(get_db)):
    curso = db.query(CourseModel).filter(CourseModel.id == course_id).first()
    if not curso:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")
    return curso

@router.post("/", response_model=CourseResponse, status_code=status.HTTP_201_CREATED)
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    novo_curso = CourseModel(**course.model_dump(exclude={"author"}))

    db.add(novo_curso)
    db.commit()
    db.refresh(novo_curso)

    return novo_curso

@router.put("/{course_id}", response_model=CourseResponse)
def update_course(course_id: int, course: CourseUpdate, db: Session = Depends(get_db)):
    curso = db.query(CourseModel).filter(CourseModel.id == course_id).first()
    if not curso:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")

    for key, value in course.model_dump(exclude_unset=True).items():
        setattr(curso, key, value)

    db.commit()
    db.refresh(curso)

    return curso
    

@router.delete("/{course_id}")
def delete_course(course_id: int, db: Session = Depends(get_db)):
    curso = db.query(CourseModel).filter(CourseModel.id == course_id).first()

    if not curso:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")
    
    db.delete(curso)
    db.commit()
        
    return {"message": "Curso deletado com sucesso"}


