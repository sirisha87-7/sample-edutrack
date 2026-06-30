from datetime import datetime

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from src.models.userModel import User
from src.models.courseModel import Course
from src.models.enrollmentModel import Enrollment
from src.models.achievementModel import Achievement


def create_enrollment(user_id: int, course_id: int, db: Session):

    # Check user
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    # Check course
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Course not found"
        )

    # Prevent duplicate active enrollment
    enrollment = (
        db.query(Enrollment)
        .filter(
            Enrollment.user_id == user_id,
            Enrollment.course_id == course_id,
            Enrollment.status == "active"
        )
        .first()
    )

    if enrollment:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already enrolled in this course."
        )

    enrollment = Enrollment(
        user_id=user_id,
        course_id=course_id,
        completed_lessons_count=0,
        status="active"
    )

    db.add(enrollment)
    db.commit()
    db.refresh(enrollment)

    return enrollment


def complete_lesson(enrollment_id: int, db: Session):

    enrollment = (
        db.query(Enrollment)
        .filter(Enrollment.id == enrollment_id)
        .first()
    )

    if not enrollment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Enrollment not found."
        )

    if enrollment.status == "completed":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Course already completed."
        )

    course = enrollment.course

    if enrollment.completed_lessons_count >= course.total_lessons:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="All lessons are already completed."
        )

    # Increment lesson count
    enrollment.completed_lessons_count += 1

    # Mark course as completed
    if enrollment.completed_lessons_count == course.total_lessons:

        enrollment.status = "completed"
        enrollment.completed_at = datetime.utcnow()

        # ---------------- Fast Starter ----------------

        completed_courses = (
            db.query(Enrollment)
            .filter(
                Enrollment.user_id == enrollment.user_id,
                Enrollment.status == "completed"
            )
            .count()
        )

        if completed_courses == 1:
            exists = (
                db.query(Achievement)
                .filter(
                    Achievement.user_id == enrollment.user_id,
                    Achievement.title == "Fast Starter"
                )
                .first()
            )

            if not exists:
                db.add(
                    Achievement(
                        user_id=enrollment.user_id,
                        title="Fast Starter"
                    )
                )

        # ---------------- Deep Diver ----------------

        if course.total_lessons >= 10:

            exists = (
                db.query(Achievement)
                .filter(
                    Achievement.user_id == enrollment.user_id,
                    Achievement.title == "Deep Diver"
                )
                .first()
            )

            if not exists:
                db.add(
                    Achievement(
                        user_id=enrollment.user_id,
                        title="Deep Diver"
                    )
                )

    db.commit()
    db.refresh(enrollment)

    return enrollment