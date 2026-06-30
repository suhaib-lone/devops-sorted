import typer

from devops_sorted.commands.ask import ask
from devops_sorted.commands.doctor import doctor
from devops_sorted.commands.explain import explain
from devops_sorted.commands.search import search
from devops_sorted.commands.version import version

app = typer.Typer(
    help="Offline AI-powered DevOps assistant.",
    no_args_is_help=True,
)

app.command()(ask)
app.command()(explain)
app.command()(search)
app.command()(doctor)
app.command()(version)