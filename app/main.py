import logging
from fastapi import FastAPI
from app.database import engine, Base
from app.routes import health, pastes, views

logger = logging.getLogger(__name__)

app = FastAPI()


@app.on_event("startup")
async def startup():
    logger.info("Application startup...")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.on_event("shutdown")
async def shutdown():
    logger.info("Application shutdown complete")


# register routers
app.include_router(health.router)
app.include_router(pastes.router)
app.include_router(views.router)
