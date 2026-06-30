# EduTrack - Micro-Learning Progress & Analytics API

## Overview

EduTrack is a RESTful API built using **FastAPI**, **SQLAlchemy**, and **SQLite** to manage micro-learning courses. The API allows users to enroll in courses, track lesson completion, unlock achievements automatically, and view their learning progress through a dashboard.

This project demonstrates REST API development, database design using ORM relationships, business logic implementation, and analytics using SQL aggregation queries.

---

## Tech Stack

- Python 3.10+
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic

---

## Features

### User Management

- Create a new user
- View user dashboard

### Course Enrollment

- Enroll users into available courses
- Prevent duplicate active enrollments

### Lesson Progress

- Complete lessons one at a time
- Automatically mark a course as completed
- Record course completion time

### Achievement System

Achievements are unlocked automatically based on user progress.

- **Fast Starter**
  - Awarded when a user completes their first course.

- **Deep Diver**
  - Awarded when a user completes a course containing 10 or more lessons.

### Dashboard

Returns:

- User details
- Active enrolled courses
- Course progress percentage
- Earned achievements

### Leaderboard

Returns the **Top 5 users** ranked by the total number of completed lessons using an optimized SQL aggregation query.

---

## Database Schema

The application contains four database tables:

- Users
- Courses
- Enrollments
- Achievements

---

## Seed Data

The application automatically seeds the following courses when the database is empty:

| Course           | Total Lessons |
| ---------------- | ------------- |
| Python Basics    | 5             |
| Intro to FastAPI | 3             |
| SQL 101          | 10            |

---

## Project Structure

```
src/
│
├── controller/
│   ├── analyticsController.py
│   ├── enrollmentController.py
│   └── userController.py
│
├── dto/
│   ├── analyticsDto.py
│   ├── dashboardDto.py
│   ├── enrollmentDto.py
│   └── userDto.py
│
├── models/
│   ├── achievementModel.py
│   ├── courseModel.py
│   ├── enrollmentModel.py
│   └── userModel.py
│
├── routes/
│   ├── analyticsRoutes.py
│   ├── enrollmentRoutes.py
│   └── userRoutes.py
│
├── utils/
│   ├── database.py
│   └── seed.py
│
└── main.py
```

---

## Installation

### Clone the repository

```bash
git clone <repository-url>
cd EduTrack
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
uvicorn src.main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### Users

| Method | Endpoint                     | Description         |
| ------ | ---------------------------- | ------------------- |
| POST   | `/users/create`              | Create a new user   |
| GET    | `/users/{user_id}/dashboard` | View user dashboard |

### Enrollments

| Method | Endpoint                                | Description               |
| ------ | --------------------------------------- | ------------------------- |
| POST   | `/enrollments/create`                   | Enroll a user in a course |
| POST   | `/enrollments/complete/{enrollment_id}` | Complete one lesson       |

### Analytics

| Method | Endpoint                 | Description                      |
| ------ | ------------------------ | -------------------------------- |
| GET    | `/analytics/leaderboard` | Top 5 users by completed lessons |

---

## Business Rules

- A user cannot have multiple active enrollments in the same course.
- Completing the final lesson automatically marks the course as completed.
- The first completed course unlocks the **Fast Starter** achievement.
- Completing a course with **10 or more lessons** unlocks the **Deep Diver** achievement.
- Progress is calculated as:

```
(completed lessons / total lessons) × 100
```

- The leaderboard is generated using SQL aggregation (`SUM`, `GROUP BY`, `ORDER BY`) instead of Python-side sorting.

---

## Author

**Batchu Sai Maneesh**
