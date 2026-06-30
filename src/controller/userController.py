from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from src.models.userModel import User
from src.models.enrollmentModel import Enrollment
from src.models.achievementModel import Achievement



def create_user(name: str, email: str, db: Session):

    existing_user = (
        db.query(User)
        .filter(User.email == email)
        .first()
    )

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already exists."
        )

    user = User(
        name=name,
        email=email
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user






def get_dashboard(user_id: int, db: Session):

    # Check if user exists
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    # Get active enrollments
    enrollments = (
        db.query(Enrollment)
        .filter(
            Enrollment.user_id == user_id,
            Enrollment.status == "active"
        )
        .all()
    )

    active_courses = []

    for enrollment in enrollments:

        progress = (
            enrollment.completed_lessons_count
            / enrollment.course.total_lessons
        ) * 100

        active_courses.append(
            {
                "course_id": enrollment.course.id,
                "title": enrollment.course.title,
                "completed_lessons": enrollment.completed_lessons_count,
                "total_lessons": enrollment.course.total_lessons,
                "progress": round(progress, 2)
            }
        )

    # Get achievements
    achievements = (
        db.query(Achievement)
        .filter(Achievement.user_id == user_id)
        .all()
    )

    return {
        "user": {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "created_at": user.created_at
        },
        "active_courses": active_courses,
        "achievements": [
            {
                "title": achievement.title,
                "unlocked_at": achievement.unlocked_at
            }
            for achievement in achievements
        ]
    }