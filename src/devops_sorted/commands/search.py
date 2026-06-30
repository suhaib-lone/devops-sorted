import typer
from devops_sorted import console, logger

def search(query: str):
    logger.info("Processing search query...")
    console.print(f"[orange3]Searching for: {query}[/orange3]")