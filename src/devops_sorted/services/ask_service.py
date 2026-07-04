from devops_sorted.clients.base import BaseLLMClient
from devops_sorted.core.config import settings

class AskService:
    """Service for handling DevOps-related questions."""

    def __init__(self, client: BaseLLMClient):
        self.client = client

    def ask_question(self, question: str) -> str:
        """Generate an answer to a DevOps question."""
        return self.client.chat(
            prompt=question,
            model=settings.model,
        )