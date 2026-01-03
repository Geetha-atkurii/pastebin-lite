import uuid
from datetime import datetime
from fastapi import HTTPException, Request
from app.models import Paste
from app.utils.pastebin_utils import now_ms

def generate_id() -> str:
    return uuid.uuid4().hex[:8]

def check_availability(paste: Paste, current_time: int):
    if paste.expires_at and current_time >= paste.expires_at:
        raise HTTPException(status_code=404, detail="Paste expired")

    if paste.max_views is not None and paste.views >= paste.max_views:
        raise HTTPException(status_code=404, detail="Paste view limit exceeded")

async def handle_fetch(paste: Paste, db, request: Request, count_view: bool):
    current_time = now_ms(request)
    check_availability(paste, current_time)

    if count_view:
        paste.views += 1
        await db.commit()

    remaining_views = (
        paste.max_views - paste.views
        if paste.max_views is not None else None
    )

    expires_at = (
        datetime.utcfromtimestamp(paste.expires_at / 1000).isoformat()
        if paste.expires_at else None
    )

    return paste.content, remaining_views, expires_at