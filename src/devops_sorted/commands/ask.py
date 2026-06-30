import typer
from devops_sorted import console, logger

def ask(question: str):
    logger.info(f"Processing question")
    console.print(f"[magenta]Received question: {question}[/magenta]")