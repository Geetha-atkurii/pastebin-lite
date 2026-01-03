from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models import Paste

async def create_paste_query(db: AsyncSession, paste: Paste):
    db.add(paste)
    await db.commit()
    await db.refresh(paste)
    return paste

async def get_paste_by_id(db: AsyncSession, paste_id: str):
    result = await db.execute(
        select(Paste).where(Paste.id == paste_id)
    )
    return result.scalar_one_or_none()

async def update_paste(db: AsyncSession, paste: Paste):
    db.add(paste)
    await db.commit()