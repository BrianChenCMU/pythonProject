# pylint: disable=E0401
# pylint: disable=W0703
# pylint: disable=R1710
# pylint: disable=W0612
# pylint: disable=E1120
# pylint: disable=R0801
"""
This is main class
"""
import click
from .works import Works


@click.command
@click.option("--bibtex", is_flag=True, help="Get the Bibtex citation")
@click.option("--ris", is_flag=True, help="Get the RIS citation")
@click.argument("request", nargs=1)
def main(request, bibtex, ris):
    """
    This is main class
    """
    work = Works(request)
    if bibtex:
        try:
            work.bibtex()
        except Exception as errormsg:
            click.echo(f"Error: {errormsg}")
            return 1
    if ris:
        try:
            work.ris()
        except Exception as errormsg:
            # click.echo(f"Error: {errormsg}")
            return 1
    if not (bibtex or ris):
        click.echo("Error: Please specify an option")
        return 1


if __name__ == "__main__":
    main()

