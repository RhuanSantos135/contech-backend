from fastapi import FastAPI
from app.routers.v1 import router


def create_application() -> FastAPI:
    application = FastAPI()
    application.include_router(router)
    return application


app = create_application()