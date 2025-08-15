from fastapi import FastAPI
from app.routers import router


def create_application() -> FastAPI:
    application = FastAPI()
    application.include_router(router)
    return application


app = create_application()