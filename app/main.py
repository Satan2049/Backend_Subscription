from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.db.init_db import init_db
from app.api.v1.users import router as user_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(title="Subscription Backend", lifespan=lifespan)

app.include_router(
    user_router,
    prefix="/api/v1/users",
    tags=["users"]
)
