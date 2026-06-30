import typer
from devops_sorted import __version__
from devops_sorted import console, logger


def version():
    logger.info("Fetching version information...")
    console.print(f"[green]DevOps-Sorted v{__version__}[/green]")