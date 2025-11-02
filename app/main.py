# app/main.py
from fastapi import FastAPI
from contextlib import asynccontextmanager
from .db import create_table
from .routes import router

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_table()
    print("✅ DynamoDB table checked or created.")
    yield
    print("🛑 Application shutting down...")

app = FastAPI(title="DynamoDB API", lifespan=lifespan)

app.include_router(router)
