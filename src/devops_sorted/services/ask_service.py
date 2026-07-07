from devops_sorted.clients.base import BaseLLMClient
from devops_sorted.core.config import settings
from devops_sorted.schemas.chat import ChatRequest
from typing import Iterator


class AskService:
    """Service for handling DevOps-related questions."""

    def __init__(self, client: BaseLLMClient):
        self.client = client

    def ask_question(self, question: str) -> Iterator[str]:
        """Generate an answer to a DevOps question."""

        request = ChatRequest(
            prompt=question,
            model=settings.model.name,
        )

        response = self.client.stream_chat(request)
        return response
        # return response.content