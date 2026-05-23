from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class CourseCreate(BaseModel):
    title: str
    description: str | None = Field(default=None, max_length=300)
    price: float = Field(gt=0, description="The price must be greater than zero")
    course_hours: int = Field(gt=0, description="The course hours must be greater than zero")
    related_topics: list[str] = []

class CourseUpdate(BaseModel):
    title: str | None
    description: str | None = Field(default=None, max_length=300)
    price: float | None = Field(default=None, gt=0, description="The price must be greater than zero")
    course_hours: int | None = Field(default=None, gt=0, description="The course hours must be greater than zero")
    related_topics: list[str] | None = None

class CourseResponse(BaseModel):
    id: int
    title: str
    description: str
    price: float
    course_hours: int
    related_topics: list[str] = []
    activated: bool
    created_at: datetime

    class Config:
        from_attributes = True

