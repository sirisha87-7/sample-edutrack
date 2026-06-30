from sqlalchemy import func, desc
from sqlalchemy.orm import Session

from src.models.userModel import User
from src.models.enrollmentModel import Enrollment


def get_leaderboard(db: Session):

    leaderboard = (
        db.query(
            User.id.label("user_id"),
            User.name,
            func.sum(
                Enrollment.completed_lessons_count
            ).label("total_lessons_completed")
        )
        .join(
            Enrollment,
            User.id == Enrollment.user_id
        )
        .group_by(
            User.id,
            User.name
        )
        .order_by(
            desc("total_lessons_completed")
        )
        .limit(5)
        .all()
    )

    return leaderboard