from fastapi import APIRouter, Depends, Request, HTTPException
from fastapi.responses import HTMLResponse
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.models import Paste
from app.services.paste_service import handle_fetch
import html

router = APIRouter(tags=["Views"])

@router.get("/p/{paste_id}", response_class=HTMLResponse)
async def view_paste(
    paste_id: str,
    request: Request,
    db: AsyncSession = Depends(get_db),
):
    paste = await db.get(Paste, paste_id)
    if not paste:
        raise HTTPException(status_code=404)

    content, _, _ = await handle_fetch(
        paste, db, request, count_view=True
    )

    return f"<pre>{html.escape(content)}</pre>"