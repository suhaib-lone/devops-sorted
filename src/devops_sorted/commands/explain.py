import typer
from devops_sorted import console, logger


def explain(command: str):
    logger.info(f"Fetching relevant information")
    console.print(f"[blue]Explaining: {command}[/blue]")