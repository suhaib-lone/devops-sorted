from typing import Iterator

import ollama

from devops_sorted.core.logger import logger
from .base import BaseLLMClient


class OllamaClient(BaseLLMClient):
    """Client wrapper around the Ollama Python SDK."""

    def __init__(self, host: str = "http://localhost:11434"):
        self._client = ollama.Client(host=host)

    def is_running(self) -> bool:
        try:
            self._client.ps()
            return True
        except Exception:
            return False

    def list_models(self) -> list[str]:
        try:
            response = self._client.list()

            models = []

            for model in response.models:
                models.append(model.model)

            return models

        except Exception as e:
            logger.error("Unable to list models: %s", e)
            return []

    def chat(self, prompt: str, model: str) -> str:
        response = self._client.chat(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return response["message"]["content"]

    def stream_chat(
        self,
        prompt: str,
        model: str,
    ) -> Iterator[str]:

        stream = self._client.chat(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            stream=True,
        )

        for chunk in stream:
            yield chunk["message"]["content"]