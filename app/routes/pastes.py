from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.ext.asyncio import AsyncSession
from app.dao.paste_dao import create_paste_query
from app.database import get_db
from app.schemas.paste_schema import (
    PasteCreateRequest,
    PasteCreateResponse,
    PasteFetchResponse,
)
from app.models import Paste
from app.services.paste_service import generate_id, handle_fetch
from app.utils.pastebin_utils import now_ms
import os

router = APIRouter(tags=["Pastes"])

@router.post("/api/pastes", response_model=PasteCreateResponse)
async def create_paste(
    payload: PasteCreateRequest,
    request: Request,
    db: AsyncSession = Depends(get_db),
):
    now = now_ms(request)

    expires_at = (
        now + payload.ttl_seconds * 1000
        if payload.ttl_seconds is not None
        else None
    )

    paste = Paste(
        id=generate_id(),
        content=payload.content,
        created_at=now,
        expires_at=expires_at,
        max_views=payload.max_views,
        views=0,
    )

    paste = await create_paste_query(db, paste)

    base_url = str(request.base_url).rstrip("/")

    return {
        "id": paste.id,
        "url": f"{base_url}/p/{paste.id}",
    }

@router.get("/api/pastes/{paste_id}", response_model=PasteFetchResponse)
async def fetch_paste(
    paste_id: str,
    request: Request,
    db: AsyncSession = Depends(get_db),
):
    paste = await db.get(Paste, paste_id)
    if not paste:
        raise HTTPException(status_code=404)

    content, remaining, expires = await handle_fetch(
        paste, db, request, count_view=True
    )

    return {
        "content": content,
        "remaining_views": remaining,
        "expires_at": expires,
    }