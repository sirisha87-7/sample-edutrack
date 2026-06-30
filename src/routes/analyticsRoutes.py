from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.utils.database import get_db

from src.dto.analyticsDto import LeaderboardResponse
from src.controller.analyticsController import get_leaderboard


analytics_routes = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)


@analytics_routes.get(
    "/leaderboard",
    response_model=list[LeaderboardResponse]
)
def get_leaderboard_endpoint(
    db: Session = Depends(get_db)
):
    return get_leaderboard(db)