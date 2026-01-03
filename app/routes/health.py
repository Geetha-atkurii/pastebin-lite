from fastapi import APIRouter

router = APIRouter(tags=["Health"])

@router.get("/api/healthz")
async def healthz():
    return {"ok": True}