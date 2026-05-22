from fastapi import APIRouter
from pydantic import BaseModel, Field

router = APIRouter(prefix="/courses", tags=["Courses"])

class Author(BaseModel):
    name: str
    age: int = Field(gt=0, lt=120, example=18, description="The age must be greater than 0 and less than 120")

class Course(BaseModel):
    title: str
    description: str | None = Field(default=None, max_length=300)
    price: float = Field(gt=0, description="The price must be greater than zero")
    author: list[Author]
    course_hours: int = Field(gt=0, description="The course hours must be greater than zero")
    related_topics: list[str] = []


@router.get("/")
def read_Courses():
    return  {"message": "Por ser um get retornaria ou uma lista de cursos local ou do banco"}

@router.post("/", status_code=201)
def create_course(course: Course):
    return {"Course": course}

@router.put("/{course_id}")
def update_course(course_id: int, course: Course):
    return {"course_id": course_id, "course": course}

@router.delete("/{course_id}")
def delete_course(course_id: int, course: Course):
    return {"message": "Curso deletado com sucesso!", "course_id": course_id}

