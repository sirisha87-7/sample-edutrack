from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.utils.database import engine, Base, local_session
from src.seed import seed_courses
from src.routes.enrollmentRoute import enrollment_routes
from src.routes.userRoute import user_routes
from src.routes.analyticsRoutes import analytics_routes

Base.metadata.create_all(bind=engine)
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup():

    Base.metadata.create_all(bind=engine)

    db = local_session()
    seed_courses(db)
    db.close()

app.include_router(enrollment_routes)
app.include_router(user_routes)
app.include_router(analytics_routes)