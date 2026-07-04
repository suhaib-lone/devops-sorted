from dataclasses import dataclass
from typing import Optional
from devops_sorted.core.config import settings
@dataclass
class ChatRequest:
    """Represents a chat request to the LLM."""
    prompt: str
    model: Optional[str] = None
    temperature: float = 0.2

@dataclass
class ChatResponse:
    content: str
    model: str = settings.model
    elapsed: Optional[float] = None