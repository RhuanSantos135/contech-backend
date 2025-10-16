from fastapi import FastAPI
from app.conf.conf import ALGORITHM
from app.routers.v1.users.users import router as users_router
application = FastAPI()

@application.get("/")
def head():
    application.include_router(users_router)
