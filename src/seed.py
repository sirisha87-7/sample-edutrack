from sqlalchemy.orm import Session

from src.models.courseModel import Course


def seed_courses(db: Session):
    if db.query(Course).count() > 0:
        return

    courses = [
        Course(
            title="Python Basics",
            description="Learn Python fundamentals.",
            total_lessons=5,
        ),
        Course(
            title="Intro to FastAPI",
            description="Build APIs using FastAPI.",
            total_lessons=3,
        ),
        Course(
            title="SQL 101",
            description="Introduction to SQL and databases.",
            total_lessons=10,
        ),
    ]

    db.add_all(courses)
    db.commit()

    print("Sample courses inserted successfully.")