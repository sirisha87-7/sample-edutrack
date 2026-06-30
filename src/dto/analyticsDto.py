from pydantic import BaseModel


class LeaderboardResponse(BaseModel):
    user_id: int
    name: str
    total_lessons_completed: int