from abc import ABC, abstractmethod

from schemas.chat import ChatRequest


class BaseProvider(ABC):

    @abstractmethod
    async def chat(self, request: ChatRequest):
        """
        Send chat completion request.
        """
        raise NotImplementedError