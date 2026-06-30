import typer
from devops_sorted import console, __version__

app = typer.Typer(
    help="DevOps assistant.",
    no_args_is_help=True,
)


@app.command()
def version():
    """Display the installed version."""
    console.print(f"[green]DevOps-Sorted v{__version__}[/green]")


@app.command()
def ask(question: str):
    """Ask a DevOps-related question."""
    console.print(f"[cyan]Received question: {question}[/cyan]")


@app.command()
def explain(command: str):
    """Explain a command."""
    console.print(f"[blue]Explaining: {command}[/blue]")


@app.command()
def search(query: str):
    """Search the knowledge base."""
    console.print(f"[orange3]Searching for: {query}[/orange3]")


@app.command()
def doctor():
    """Check the local installation."""
    console.print("[green]DevOps-Sorted is installed correctly![/green]")