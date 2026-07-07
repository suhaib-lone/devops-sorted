from rich.markdown import Markdown
from devops_sorted.core.factory import get_llm_client
from devops_sorted.core.console import console
from devops_sorted.services.ask_service import AskService


def ask(question: str) -> None:
    """Ask a DevOps-related question."""

    client = get_llm_client()
    service = AskService(client)
    response = service.ask_question(question)
    for chunk in response:
        console.print(chunk, end="")

