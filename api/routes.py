from fastapi import APIRouter

from schemas.request import ChatRequest
from schemas.response import ChatResponse
from services.chat_service import chat


router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat_endpoint(request: ChatRequest):

    answer = chat(request.query)

    return ChatResponse(
        answer=answer
    )