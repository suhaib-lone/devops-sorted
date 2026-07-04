from rich.markdown import Markdown

from devops_sorted.clients.ollama import OllamaClient
from devops_sorted.core.console import console
from devops_sorted.services.ask_service import AskService


def ask(question: str) -> None:
    """Ask a DevOps-related question."""

    client = OllamaClient()
    service = AskService(client)
    response = service.ask_question(question)

    console.print(Markdown(response))