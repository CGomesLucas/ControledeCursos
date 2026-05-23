from fastapi import APIRouter
from app.schemas.course_schema import CourseCreate, CourseResponse, CourseUpdate

router = APIRouter(prefix="/courses", tags=["Courses"])

@router.get("/",)
def read_Courses():
    return  {"message": "Por ser um get retornaria ou uma lista de cursos local ou do banco"}

@router.post("/", status_code=201)
def create_course(course: CourseCreate):
    return {"Course": course}

@router.put("/{course_id}")
def update_course(course_id: int, course: CourseUpdate):
    return {"course_id": course_id, "course": course}

@router.delete("/{course_id}")
def delete_course(course_id: int, course: CourseResponse):
    return {"message": "Curso deletado com sucesso!", "course_id": course_id}

