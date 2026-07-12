from pydantic import BaseModel, Field


class Message(BaseModel):
    role: str = Field(..., examples=["user"])
    content: str


class ChatRequest(BaseModel):
    messages: list[Message]
    model: str = "gpt-4o-mini"
    stream: bool = True


class ChatResponse(BaseModel):
    id: str | None = None
    model: str | None = None
    choices: list | None = None