import httpx

from config import settings


class LLMService:

    async def chat(self, request):

        async with httpx.AsyncClient(
            timeout=settings.REQUEST_TIMEOUT
        ) as client:

            response = await client.post(
                f"{settings.BASE_URL}/chat/completions",
                json={
                    "model": request.model,
                    "messages": [
                        m.model_dump()
                        for m in request.messages
                    ],
                    "stream": request.stream
                },
                headers={
                    "Authorization": f"Bearer {settings.API_KEY}"
                }
            )

            response.raise_for_status()

            return response.json()


llm_service = LLMService()