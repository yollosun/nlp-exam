from typing import Union
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from router import v1_router
import uvicorn as uvicorn

origins = [
    "http://localhost",
    "http://localhost:3000",
]

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# создаем движок SqlAlchemy
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
# создаем базовый класс для моделей
Base = declarative_base()

Base.metadata.create_all(bind=engine)


def create_app() -> FastAPI:
    current_app = FastAPI(
        title="Asynchronous tasks processing with Celery and RabbitMQ",
        description="Sample FastAPI Application to demonstrate Event "
        "driven architecture with Celery and RabbitMQ",
        version="1.0.0",
    )

    current_app.include_router(v1_router.router)

    current_app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return current_app


app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", port=9000, reload=True)
