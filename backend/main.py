from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import httpx
from config import settings

app = FastAPI(title=settings.APP_NAME, version=settings.VERSION)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    messages: list
    model: str = "gpt-4o"
    stream: bool = True

@app.post("/api/chat")
async def chat_completion(request: ChatRequest):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "https://api.gapgpt.app/v1/chat/completions",  # یا هر پراکسی که می‌خوای
                json={
                    "model": request.model,
                    "messages": request.messages,
                    "stream": request.stream
                },
                headers={"Authorization": f"Bearer {YOUR_API_KEY}"},  # از env بخون
                timeout=120.0
            )
            return response.json()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health():
    return {"status": "healthy", "app": settings.APP_NAME}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=settings.API_HOST, port=settings.API_PORT)