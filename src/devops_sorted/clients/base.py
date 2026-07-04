from abc import ABC, abstractmethod
from devops_sorted.schemas.chat import ChatRequest, ChatResponse
from typing import Iterator


class BaseLLMClient(ABC):
    """Abstract base class for LLM clients."""

    @abstractmethod
    def is_running(self) -> bool:
        """Return True if the backend is available."""
        raise NotImplementedError

    @abstractmethod
    def list_models(self) -> list[str]:
        """Return available models."""
        raise NotImplementedError

    @abstractmethod
    def chat(self, request: ChatRequest) -> ChatResponse:
        """Return a complete response."""
        raise NotImplementedError

    @abstractmethod
    def stream_chat(self, request: ChatRequest) -> Iterator[str]:
        """Yield response tokens."""
        raise NotImplementedError