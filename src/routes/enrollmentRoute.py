from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from src.utils.database import get_db

from src.dto.enrollmentDto import (
    EnrollmentCreate,
    EnrollmentResponse
)

from src.controller.enrollmentController import create_enrollment, complete_lesson

enrollment_routes = APIRouter(
    prefix="/enrollments",
    tags=["Enrollments"]
)



@enrollment_routes.post(
    "/create",
    response_model=EnrollmentResponse,
    status_code=status.HTTP_201_CREATED
)
def create_enrollment_endpoint(
    body: EnrollmentCreate,
    db: Session = Depends(get_db)
):
    return create_enrollment(
        body.user_id,
        body.course_id,
        db
    )



@enrollment_routes.post(
    "/complete/{enrollment_id}",
    response_model=EnrollmentResponse,
    status_code=status.HTTP_200_OK
)
def complete_lesson_endpoint(
    enrollment_id: int,
    db: Session = Depends(get_db)
):
    return complete_lesson(
        enrollment_id,
        db
    )