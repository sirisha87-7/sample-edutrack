from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from src.utils.database import get_db

from src.dto.dashboardDto import DashboardResponse

from src.controller.userController import get_dashboard, create_user

from src.dto.userDto import UserCreate, UserResponse

user_routes = APIRouter(
    prefix="/users",
    tags=["Users"]
)



@user_routes.post(
    "/create",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
def create_user_endpoint(
    body: UserCreate,
    db: Session = Depends(get_db)
):
    return create_user(
        body.name,
        body.email,
        db
    )

@user_routes.get(
    "/{user_id}/dashboard",
    response_model=DashboardResponse
)
def get_dashboard_endpoint(
    user_id: int,
    db: Session = Depends(get_db)
):
    return get_dashboard(
        user_id,
        db
    )