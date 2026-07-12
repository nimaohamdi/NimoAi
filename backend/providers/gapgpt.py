import httpx

from config import settings
from schemas.chat import ChatRequest
from providers.base import BaseProvider


class GapGPTProvider(BaseProvider):

    async def chat(self, request: ChatRequest):

        async with httpx.AsyncClient(
            timeout=settings.REQUEST_TIMEOUT
        ) as client:

            response = await client.post(
                f"{settings.BASE_URL}/chat/completions",
                headers={
                    "Authorization": f"Bearer {settings.API_KEY}"
                },
                json={
                    "model": request.model,
                    "messages": [
                        message.model_dump()
                        for message in request.messages
                    ],
                    "stream": request.stream
                }
            )

            response.raise_for_status()

            return response.json()