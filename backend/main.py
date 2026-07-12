from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config import settings
from api.chat import router as chat_router

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    chat_router,
    prefix="/api",
    tags=["Chat"]
)


@app.get("/health")
async def health():

    return {
        "status": "healthy",
        "version": settings.VERSION
    }


if __name__ == "__main__":

    import uvicorn

    uvicorn.run(
        app,
        host=settings.API_HOST,
        port=settings.API_PORT
    )