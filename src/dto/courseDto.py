from pydantic import BaseModel, ConfigDict


class CourseResponse(BaseModel):
    id: int
    title: str
    description: str
    total_lessons: int

    model_config = ConfigDict(from_attributes=True)