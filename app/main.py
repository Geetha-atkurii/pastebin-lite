import logging
from fastapi import FastAPI
from app.database import engine, Base

app = FastAPI()

logger = logging.getLogger(__name__)


@app.on_event("startup")
async def startup():
    logger.info("Application startup...")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.get("/api/healthz")
async def healthz():
    return {"ok": True}
