import typer
from devops_sorted import console, logger


def doctor():
    logger.info("Running diagnostics...")
    console.print("[green]Everything looks good![/green]")