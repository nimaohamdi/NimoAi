from fastapi import APIRouter, HTTPException

from schemas.chat import ChatRequest
from services.llm_service import llm_service

router = APIRouter()


@router.post("/chat")
async def chat(request: ChatRequest):

    try:
        return await llm_service.chat(request)

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )