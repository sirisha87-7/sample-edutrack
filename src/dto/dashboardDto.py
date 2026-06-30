from pydantic import BaseModel


class ActiveCourse(BaseModel):
    course_id: int
    title: str
    completed_lessons: int
    total_lessons: int
    progress: float


class DashboardResponse(BaseModel):
    user: dict
    active_courses: list[ActiveCourse]
    achievements: list[dict]


class LeaderboardResponse(BaseModel):
    user_id: int
    name: str
    total_lessons_completed: int