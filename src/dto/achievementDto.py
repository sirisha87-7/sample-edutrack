from datetime import datetime

from pydantic import BaseModel, ConfigDict


class AchievementResponse(BaseModel):
    id: int
    title: str
    unlocked_at: datetime

    model_config = ConfigDict(from_attributes=True)